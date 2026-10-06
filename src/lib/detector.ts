/**
 * WEBNOX - Rule-Based Phishing Risk Detection Engine (TypeScript / Serverless)
 * ----------------------------------------------------------------------------
 * A transparent, lightweight rule-based detector that analyzes URL features
 * and assigns calibrated risk scores (0-100) with explainable reasons.
 */

export interface DetectionResult {
  url: string;
  risk_score: number;
  verdict: 'safe' | 'suspicious' | 'phishing';
  confidence: number;
  reasons: string[];
  recommendation: string;
}

// Well-known high-authority root domains (verified safe baselines)
const KNOWN_SAFE_DOMAINS = new Set([
  'google.com',
  'microsoft.com',
  'github.com',
  'wikipedia.org',
  'apple.com',
  'amazon.com',
  'paypal.com',
  'youtube.com',
  'linkedin.com',
  'twitter.com',
  'x.com',
  'netflix.com',
  'cloudflare.com',
  'stackoverflow.com',
  'vercel.com',
]);

// Major target brands frequently targeted by phishing campaigns
const MAJOR_BRANDS = [
  'paypal',
  'google',
  'microsoft',
  'amazon',
  'apple',
  'netflix',
  'chase',
  'wellsfargo',
  'bankofamerica',
  'facebook',
  'instagram',
  'binance',
  'coinbase',
  'dropbox',
];

// High-risk authentication / financial keywords
const SUSPICIOUS_KEYWORDS = [
  'login',
  'verify',
  'account',
  'password',
  'secure',
  'payment',
  'banking',
  'update',
  'signin',
  'wallet',
  'confirm',
  'security',
  'authenticate',
  'credential',
  'billing',
];

// Top-level domains frequently abused for disposable phishing campaigns
const SUSPICIOUS_TLDS = new Set([
  'xyz',
  'top',
  'tk',
  'ml',
  'ga',
  'cf',
  'gq',
  'buzz',
  'cam',
  'live',
  'icu',
  'work',
  'click',
  'link',
  'rest',
  'fit',
  'surf',
  'monster',
  'club',
]);

export function analyzeUrl(rawUrl: string): DetectionResult {
  // 1. Normalize URL
  const url = (rawUrl || '').trim();
  if (!url) {
    return {
      url: rawUrl,
      risk_score: 0,
      verdict: 'safe',
      confidence: 50,
      reasons: ['Empty URL provided'],
      recommendation: 'Please enter a valid URL.',
    };
  }

  // Prepend https:// if no protocol provided for parsing
  const withProtocol = /^https?:\/\//i.test(url) ? url : `https://${url}`;

  let parsed: URL;
  try {
    parsed = new URL(withProtocol);
  } catch {
    return {
      url: rawUrl,
      risk_score: 85,
      verdict: 'phishing',
      confidence: 80,
      reasons: ['Malformed URL syntax'],
      recommendation: 'Avoid visiting malformed web addresses.',
    };
  }

  const hostname = (parsed.hostname || '').toLowerCase();
  const path = (parsed.pathname || '').toLowerCase();
  const fullLower = url.toLowerCase();
  const reasons: string[] = [];
  let riskScore = 0;

  // Fast-path for verified genuine authority domains
  let isGenuineBrand = false;
  for (const safeDomain of KNOWN_SAFE_DOMAINS) {
    if (hostname === safeDomain || hostname.endsWith(`.${safeDomain}`)) {
      isGenuineBrand = true;
      break;
    }
  }

  // If it's a genuine verified safe domain without suspicious tricks, return safe
  if (isGenuineBrand && !fullLower.includes('@') && !hostname.includes('xn--')) {
    return {
      url: rawUrl,
      risk_score: 5,
      verdict: 'safe',
      confidence: 92,
      reasons: [
        `Verified high-reputation domain (${hostname})`,
        'No major suspicious URL patterns detected',
      ],
      recommendation: 'Website appears relatively safe.',
    };
  }

  // -------------------------------------------------------------
  // RULE 1: Protocol Security (HTTP vs HTTPS)
  // -------------------------------------------------------------
  if (parsed.protocol === 'http:') {
    riskScore += 15;
    reasons.push('Unencrypted connection: Uses HTTP instead of secure HTTPS');
  }

  // -------------------------------------------------------------
  // RULE 2: IP Address in Hostname (Raw IP URL)
  // -------------------------------------------------------------
  const ipPattern = /^(\d{1,3}\.){3}\d{1,3}(:\d+)?$/;
  if (ipPattern.test(hostname)) {
    riskScore += 35;
    reasons.push('Host uses a raw IP address instead of a registered domain name');
  }

  // -------------------------------------------------------------
  // RULE 3: Punycode / IDN Homoglyphs (xn--)
  // -------------------------------------------------------------
  if (hostname.includes('xn--')) {
    riskScore += 30;
    reasons.push('Punycode (xn--) detected: Possible internationalized homoglyph spoofing');
  }

  // -------------------------------------------------------------
  // RULE 4: Obvious Brand Impersonation Patterns
  // -------------------------------------------------------------
  let foundBrand: string | null = null;
  for (const brand of MAJOR_BRANDS) {
    if (fullLower.includes(brand)) {
      const officialDomain = `${brand}.com`;
      if (hostname !== officialDomain && !hostname.endsWith(`.${officialDomain}`)) {
        foundBrand = brand;
        riskScore += 35;
        reasons.push(
          `Possible brand impersonation: Target brand '${brand}' found on an unauthorized domain`
        );
        break;
      }
    }
  }

  // -------------------------------------------------------------
  // RULE 5: Suspicious Top-Level Domains (TLDs)
  // -------------------------------------------------------------
  const parts = hostname.split('.');
  const tld = parts.length > 1 ? parts[parts.length - 1] : '';
  if (SUSPICIOUS_TLDS.has(tld)) {
    riskScore += 20;
    reasons.push(
      `Uses high-risk TLD (.${tld}) frequently leveraged by disposable phishing sites`
    );
  }

  // -------------------------------------------------------------
  // RULE 6: Sensitive Authentication / Financial Keywords
  // -------------------------------------------------------------
  const foundKeywords = SUSPICIOUS_KEYWORDS.filter((kw) => fullLower.includes(kw));
  if (foundKeywords.length > 0) {
    if (foundKeywords.length >= 2 || foundBrand) {
      riskScore += 25;
      reasons.push(
        `Contains multiple sensitive keywords: ${foundKeywords.slice(0, 3).join(', ')}`
      );
    } else {
      riskScore += 15;
      reasons.push(`Contains sensitive keyword in URL: ${foundKeywords[0]}`);
    }
  }

  // -------------------------------------------------------------
  // RULE 7: Excessive Subdomains
  // -------------------------------------------------------------
  const subdomainCount = Math.max(0, parts.length - 2);
  if (subdomainCount >= 3) {
    riskScore += 20;
    reasons.push(`Excessive subdomains detected (${subdomainCount} levels)`);
  } else if (subdomainCount === 2 && !hostname.endsWith('.co.uk') && !hostname.endsWith('.co.in')) {
    riskScore += 10;
    reasons.push('Unusual subdomain nesting detected');
  }

  // -------------------------------------------------------------
  // RULE 8: Suspicious Symbols & Obfuscation
  // -------------------------------------------------------------
  if (fullLower.includes('@')) {
    riskScore += 25;
    reasons.push("Contains '@' symbol, a common tactic to disguise actual destination");
  }

  const hyphenCount = (hostname.match(/-/g) || []).length;
  if (hyphenCount >= 2) {
    riskScore += 15;
    reasons.push(
      `Excessive hyphens in hostname (${hyphenCount} hyphens), typical of deceptive domains`
    );
  }

  if (path.includes('//')) {
    riskScore += 10;
    reasons.push("Path contains double slashes ('//') indicating possible open redirect");
  }

  // -------------------------------------------------------------
  // RULE 9: Unusually Long URLs
  // -------------------------------------------------------------
  if (url.length > 100) {
    riskScore += 15;
    reasons.push('Excessively long URL (over 100 characters)');
  } else if (url.length > 75) {
    riskScore += 10;
    reasons.push('Unusually long URL (over 75 characters)');
  }

  // -------------------------------------------------------------
  // Final Scoring & Verdict Mapping
  // -------------------------------------------------------------
  let finalScore = Math.min(Math.max(riskScore, 0), 100);

  if (finalScore === 0) {
    finalScore = 10;
    reasons.push('No major suspicious URL patterns detected');
  }

  let verdict: 'safe' | 'suspicious' | 'phishing';
  let recommendation: string;

  if (finalScore <= 30) {
    verdict = 'safe';
    recommendation = 'Website appears relatively safe. Exercise normal browsing caution.';
  } else if (finalScore <= 60) {
    verdict = 'suspicious';
    recommendation = 'Proceed with caution. Avoid entering sensitive passwords or payment details.';
  } else {
    verdict = 'phishing';
    recommendation =
      'Do not enter passwords, OTPs, or personal information. High probability of phishing.';
  }

  const confidence = Math.min(75 + reasons.length * 5, 95);

  return {
    url: rawUrl,
    risk_score: finalScore,
    verdict,
    confidence,
    reasons,
    recommendation,
  };
}
