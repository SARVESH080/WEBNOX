"""
PhishGuard - Rule-Based Phishing Risk Detection Engine
------------------------------------------------------
A transparent, lightweight rule-based detector that analyzes URL features
and assigns calibrated risk scores (0-100) with explainable reasons.
"""

import re
from urllib.parse import urlparse

# Well-known high-authority root domains (verified safe baselines)
KNOWN_SAFE_DOMAINS = {
    "google.com",
    "microsoft.com",
    "github.com",
    "wikipedia.org",
    "apple.com",
    "amazon.com",
    "paypal.com",
    "youtube.com",
    "linkedin.com",
    "twitter.com",
    "x.com",
    "netflix.com",
    "cloudflare.com",
    "stackoverflow.com",
    "vercel.com",
}

# Major target brands frequently targeted by phishing campaigns
MAJOR_BRANDS = [
    "paypal",
    "google",
    "microsoft",
    "amazon",
    "apple",
    "netflix",
    "chase",
    "wellsfargo",
    "bankofamerica",
    "facebook",
    "instagram",
    "binance",
    "coinbase",
    "dropbox",
]

# High-risk authentication / financial keywords
SUSPICIOUS_KEYWORDS = [
    "login",
    "verify",
    "account",
    "password",
    "secure",
    "payment",
    "banking",
    "update",
    "signin",
    "wallet",
    "confirm",
    "security",
    "authenticate",
    "credential",
    "billing",
]

# Top-level domains frequently abused for disposable phishing campaigns
SUSPICIOUS_TLDS = {
    "xyz",
    "top",
    "tk",
    "ml",
    "ga",
    "cf",
    "gq",
    "buzz",
    "cam",
    "live",
    "icu",
    "work",
    "click",
    "link",
    "rest",
    "fit",
    "surf",
    "monster",
    "club",
}


def analyze_url(raw_url: str) -> dict:
    """
    Analyzes a given URL against transparent phishing risk rules.
    Returns risk score, verdict ('safe' | 'suspicious' | 'phishing'),
    confidence percentage, triggered reasons, and recommendations.
    """
    # 1. Normalize URL
    url = raw_url.strip()
    if not url:
        return {
            "url": raw_url,
            "risk_score": 0,
            "verdict": "safe",
            "confidence": 50,
            "reasons": ["Empty URL provided"],
            "recommendation": "Please enter a valid URL.",
        }

    # Prepend https:// if no protocol provided for parsing
    if not re.match(r"^https?://", url, re.IGNORECASE):
        url = "https://" + url

    try:
        parsed = urlparse(url)
    except Exception:
        return {
            "url": raw_url,
            "risk_score": 85,
            "verdict": "phishing",
            "confidence": 80,
            "reasons": ["Malformed URL syntax"],
            "recommendation": "Avoid visiting malformed web addresses.",
        }

    hostname = (parsed.hostname or "").lower()
    path = (parsed.path or "").lower()
    full_lower = url.lower()
    reasons = []
    risk_score = 0

    # Fast-path for verified genuine authority domains
    is_genuine_brand = False
    for safe_domain in KNOWN_SAFE_DOMAINS:
        if hostname == safe_domain or hostname.endswith("." + safe_domain):
            is_genuine_brand = True
            break

    # If it's a genuine verified safe domain without suspicious tricks, return safe
    if is_genuine_brand and "@" not in full_lower and "xn--" not in hostname:
        return {
            "url": raw_url,
            "risk_score": 5,
            "verdict": "safe",
            "confidence": 92,
            "reasons": [
                f"Verified high-reputation domain ({hostname})",
                "No major suspicious URL patterns detected",
            ],
            "recommendation": "Website appears relatively safe.",
        }

    # -------------------------------------------------------------
    # RULE 1: Protocol Security (HTTP vs HTTPS)
    # -------------------------------------------------------------
    if parsed.scheme.lower() == "http":
        risk_score += 15
        reasons.append("Unencrypted connection: Uses HTTP instead of secure HTTPS")

    # -------------------------------------------------------------
    # RULE 2: IP Address in Hostname (Raw IP URL)
    # -------------------------------------------------------------
    ip_pattern = r"^(\d{1,3}\.){3}\d{1,3}(:\d+)?$"
    if re.match(ip_pattern, hostname):
        risk_score += 35
        reasons.append("Host uses a raw IP address instead of a registered domain name")

    # -------------------------------------------------------------
    # RULE 3: Punycode / IDN Homoglyphs (xn--)
    # -------------------------------------------------------------
    if "xn--" in hostname:
        risk_score += 30
        reasons.append("Punycode (xn--) detected: Possible internationalized homoglyph spoofing")

    # -------------------------------------------------------------
    # RULE 4: Obvious Brand Impersonation Patterns
    # -------------------------------------------------------------
    found_brand = None
    for brand in MAJOR_BRANDS:
        if brand in full_lower:
            # Check if this hostname is the official domain of that brand
            official_domain = f"{brand}.com"
            if hostname != official_domain and not hostname.endswith("." + official_domain):
                found_brand = brand
                risk_score += 35
                reasons.append(
                    f"Possible brand impersonation: Target brand '{brand}' found on an unauthorized domain"
                )
                break

    # -------------------------------------------------------------
    # RULE 5: Suspicious Top-Level Domains (TLDs)
    # -------------------------------------------------------------
    parts = hostname.split(".")
    tld = parts[-1] if len(parts) > 1 else ""
    if tld in SUSPICIOUS_TLDS:
        risk_score += 20
        reasons.append(
            f"Uses high-risk TLD (.{tld}) frequently leveraged by disposable phishing sites"
        )

    # -------------------------------------------------------------
    # RULE 6: Sensitive Authentication / Financial Keywords
    # -------------------------------------------------------------
    found_keywords = [kw for kw in SUSPICIOUS_KEYWORDS if kw in full_lower]
    if found_keywords:
        if len(found_keywords) >= 2 or found_brand:
            risk_score += 25
            reasons.append(
                f"Contains multiple sensitive keywords: {', '.join(found_keywords[:3])}"
            )
        else:
            risk_score += 15
            reasons.append(
                f"Contains sensitive keyword in URL: {found_keywords[0]}"
            )

    # -------------------------------------------------------------
    # RULE 7: Excessive Subdomains
    # -------------------------------------------------------------
    subdomain_count = max(0, len(parts) - 2)
    if subdomain_count >= 3:
        risk_score += 20
        reasons.append(f"Excessive subdomains detected ({subdomain_count} levels)")
    elif subdomain_count == 2 and not hostname.endswith((".co.uk", ".com.au", ".co.in")):
        risk_score += 10
        reasons.append("Unusual subdomain nesting detected")

    # -------------------------------------------------------------
    # RULE 8: Suspicious Symbols & Obfuscation
    # -------------------------------------------------------------
    if "@" in full_lower:
        risk_score += 25
        reasons.append("Contains '@' symbol, a common tactic to disguise actual destination")

    # Excessive hyphens in domain name (look-alike tactics)
    hyphen_count = hostname.count("-")
    if hyphen_count >= 2:
        risk_score += 15
        reasons.append(
            f"Excessive hyphens in hostname ({hyphen_count} hyphens), typical of deceptive domains"
        )

    # Double slashes in URL path (redirection obfuscation)
    if "//" in path:
        risk_score += 10
        reasons.append("Path contains double slashes ('//') indicating possible open redirect")

    # -------------------------------------------------------------
    # RULE 9: Unusually Long URLs
    # -------------------------------------------------------------
    if len(url) > 100:
        risk_score += 15
        reasons.append("Excessively long URL (over 100 characters)")
    elif len(url) > 75:
        risk_score += 10
        reasons.append("Unusually long URL (over 75 characters)")

    # -------------------------------------------------------------
    # Final Scoring & Verdict Mapping
    # -------------------------------------------------------------
    # Clamp score between 0 and 100
    final_score = min(max(risk_score, 0), 100)

    # If no flags triggered, provide a baseline safe score
    if final_score == 0:
        final_score = 10
        reasons = ["No major suspicious URL patterns detected"]

    # Assign verdicts based on strict user requirements:
    # 0–30: SAFE
    # 31–60: SUSPICIOUS
    # 61–100: PHISHING
    if final_score <= 30:
        verdict = "safe"
        recommendation = "Website appears relatively safe. Exercise normal browsing caution."
    elif final_score <= 60:
        verdict = "suspicious"
        recommendation = (
            "Proceed with caution. Avoid entering sensitive passwords or payment details."
        )
    else:
        verdict = "phishing"
        recommendation = (
            "Do not enter passwords, OTPs, or personal information. High probability of phishing."
        )

    # Compute a reasonable confidence score (75% - 95%)
    confidence = min(75 + len(reasons) * 5, 95)

    return {
        "url": raw_url,
        "risk_score": final_score,
        "verdict": verdict,
        "confidence": confidence,
        "reasons": reasons,
        "recommendation": recommendation,
    }
