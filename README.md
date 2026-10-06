# WEBNOX — Real-Time Phishing Detection

Real-Time Phishing Detection engine and cybersecurity dashboard built with Next.js 14 and Tailwind CSS, featuring a native serverless risk-analysis API route ready for direct deployment on **Vercel**.

---

## ⚡ Serverless Architecture (No Separate Backend Needed!)

The detection engine runs natively as a Next.js Serverless Route Handler (`/api/analyze`):

```text
[ Browser / User ]
       │
       ▼  (POST /api/analyze)
[ Next.js Serverless API ] ──► [ Rule-Based Risk Engine (detector.ts) ]
       │
       ▼
[ Calculated Risk Score (0-100) + Verdict + Specific Reasons ]
```

* **Zero External Servers:** Runs directly in Next.js. No Python or FastAPI server required!
* **Vercel Native:** Deploys with 1 click to Vercel without configuring environment variables.
* **Low Latency:** Analyses URLs in < 20ms using in-memory rule heuristics.

---

## 📁 Project Structure

```text
WEBNOX/
├── src/
│   ├── app/
│   │   ├── api/
│   │   │   └── analyze/
│   │   │       └── route.ts         # Native Serverless API (POST /api/analyze)
│   │   ├── layout.tsx               # Root layout & dark theme metadata
│   │   ├── page.tsx                 # Main web dashboard
│   │   └── globals.css              # Cyber dark theme styles
│   ├── components/phishguard/
│   │   ├── Navbar.tsx               # Header with WEBNOX branding
│   │   ├── HeroScanner.tsx          # URL input, preset demo targets, live scanner
│   │   ├── ResultCard.tsx           # Risk score gauge, reasons, recommendations
│   │   ├── HowItWorks.tsx           # 7-stage progressive pipeline breakdown
│   │   └── Footer.tsx               # Clean cybersecurity footer
│   └── lib/
│       ├── detector.ts              # Rule-based phishing risk engine
│       └── api.ts                   # Client that calls /api/analyze
│
├── backend/                         # Optional standalone Python FastAPI backend
│   ├── main.py                      # (Kept for standalone microservice testing)
│   ├── detector.py
│   └── requirements.txt
│
├── package.json
└── README.md
```

---

## 🚀 Quick Start (Local Development)

```bash
npm install
npm run dev
```

Open your browser at:
👉 **[http://localhost:3000](http://localhost:3000)**

---

## 🌐 1-Click Deployment to Vercel

Because the detection engine is now a serverless API route (`/api/analyze`), deploying to Vercel requires **zero server configuration**:

1. Push this project to your GitHub:
   ```bash
   git add .
   git commit -m "Deploy WEBNOX serverless application"
   git push origin main
   ```
2. Go to **[vercel.com](https://vercel.com)** ➔ Click **"Add New Project"** ➔ Select your repository.
3. Click **"Deploy"**.

Vercel will automatically build the Next.js frontend and host the `/api/analyze` serverless function globally on edge/serverless infrastructure.

---

## 📡 API Specification

### `POST /api/analyze`

#### Request Body
```json
{
  "url": "https://amazon-login-security.xyz"
}
```

#### Response Body
```json
{
  "url": "https://amazon-login-security.xyz",
  "risk_score": 95,
  "verdict": "phishing",
  "confidence": 95,
  "reasons": [
    "Possible brand impersonation: Target brand 'amazon' found on an unauthorized domain",
    "Uses high-risk TLD (.xyz) frequently leveraged by disposable phishing sites",
    "Contains multiple sensitive keywords: login, security",
    "Excessive hyphens in hostname (2 hyphens), typical of deceptive domains"
  ],
  "recommendation": "Do not enter passwords, OTPs, or personal information. High probability of phishing."
}
```

---

## 🎯 Scoring & Verdict Criteria

| Score Range | Verdict | Indicator | Meaning |
| :---: | :---: | :---: | :--- |
| **0 – 30** | `safe` | 🟢 SAFE | Verified legitimate domain or no suspicious indicators |
| **31 – 60** | `suspicious` | 🟠 SUSPICIOUS | Newly registered domain, HTTP, unverified keywords, anomalous structure |
| **61 – 100** | `phishing` | 🔴 PHISHING | Brand impersonation, disposable TLD, credential harvesting keywords, raw IP |
