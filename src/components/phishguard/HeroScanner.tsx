'use client';

import React, { useState } from 'react';
import {
  Search,
  Shield,
  Loader2,
  CheckCircle2,
  AlertTriangle,
  ShieldAlert,
  Zap,
  Server,
  AlertOctagon
} from 'lucide-react';
import { analyzeUrlWithBackend, BackendAnalyzeResponse, API_BASE_URL } from '@/lib/api';
import { analyzeUrl as localAnalyzeFallback } from '@/lib/phishHeuristics';
import { ResultCard, DisplayResult } from './ResultCard';

const DEMO_PRESETS = [
  {
    label: 'amazon-login-security.xyz',
    url: 'https://amazon-login-security.xyz',
    type: 'danger',
    tag: 'Phishing Demo'
  },
  {
    label: 'paypal-verification-example.xyz',
    url: 'https://paypal-verification-example.xyz',
    type: 'danger',
    tag: 'Phishing Demo'
  },
  {
    label: 'microsoft-account-verify.xyz',
    url: 'https://microsoft-account-verify.xyz',
    type: 'danger',
    tag: 'Phishing Demo'
  },
  {
    label: 'secure-account-verify.net',
    url: 'https://secure-account-verify.net/login',
    type: 'warning',
    tag: 'Suspicious Demo'
  },
  {
    label: 'google.com',
    url: 'https://google.com',
    type: 'safe',
    tag: 'Safe Demo'
  },
  {
    label: 'github.com',
    url: 'https://github.com',
    type: 'safe',
    tag: 'Safe Demo'
  }
];

export const HeroScanner: React.FC = () => {
  const [urlInput, setUrlInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [loadingStep, setLoadingStep] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const [isBackendError, setIsBackendError] = useState(false);
  const [result, setResult] = useState<DisplayResult | null>(null);

  const normalizeUrlDetails = (urlStr: string) => {
    try {
      const withProto = /^https?:\/\//i.test(urlStr) ? urlStr : `https://${urlStr}`;
      const parsed = new URL(withProto);
      return {
        protocol: parsed.protocol.replace(':', ''),
        hostname: parsed.hostname,
        pathname: parsed.pathname || '/',
      };
    } catch {
      return {
        protocol: 'https',
        hostname: urlStr.replace(/^https?:\/\//i, '').split('/')[0] || urlStr,
        pathname: '/',
      };
    }
  };

  const handleScan = async (urlToScan?: string, forceOffline: boolean = false) => {
    const target = (urlToScan || urlInput).trim();
    if (!target) {
      setErrorMessage('Please enter or select a website URL to analyze.');
      setIsBackendError(false);
      return;
    }

    setErrorMessage('');
    setIsBackendError(false);
    setLoading(true);
    setResult(null);

    setLoadingStep('Running serverless rule-based analysis (POST /api/analyze)...');
    const startTime = Date.now();

    if (forceOffline) {
      // Offline fallback mode
      setTimeout(() => {
        const local = localAnalyzeFallback(target);
        const details = normalizeUrlDetails(target);
        setResult({
          url: target,
          risk_score: local.riskScore,
          verdict: local.status === 'SAFE' ? 'safe' : local.status === 'SUSPICIOUS' ? 'suspicious' : 'phishing',
          confidence: 85,
          reasons: local.reasons.map(r => r.title),
          recommendation: local.summary,
          latencyMs: Date.now() - startTime,
          timestamp: new Date().toLocaleTimeString(),
          ...details,
        });
        setLoading(false);
        setLoadingStep('');
      }, 500);
      return;
    }

    try {
      // REAL SERVERLESS API CALL to /api/analyze
      const backendData = await analyzeUrlWithBackend(target);
      const latencyMs = Math.max(Date.now() - startTime, 15);
      const details = normalizeUrlDetails(backendData.url || target);

      setResult({
        ...backendData,
        latencyMs,
        timestamp: new Date().toLocaleTimeString(),
        ...details,
      });
    } catch (err: any) {
      console.error('Scan error:', err);
      const message = err?.message || 'Connection failed';
      setErrorMessage(`URL Analysis Error: ${message}`);
    } finally {
      setLoading(false);
      setLoadingStep('');
    }
  };

  const handlePresetClick = (presetUrl: string) => {
    setUrlInput(presetUrl);
    handleScan(presetUrl);
  };

  return (
    <section id="hero" className="relative pt-12 pb-20 px-4 sm:px-6 lg:px-8 max-w-6xl mx-auto">
      {/* Background Glow Accents */}
      <div className="absolute top-10 left-1/2 -translate-x-1/2 w-[600px] h-[350px] bg-cyber-cyan/[0.06] rounded-full blur-[140px] pointer-events-none -z-10" />
      <div className="absolute top-20 right-10 w-[350px] h-[250px] bg-cyber-blue/[0.05] rounded-full blur-[120px] pointer-events-none -z-10" />

      {/* Hero Header */}
      <div className="text-center max-w-3xl mx-auto">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyber-card border border-cyber-border text-xs font-mono text-cyber-cyan mb-6 shadow-sm">
          <Zap className="w-3.5 h-3.5 text-cyber-cyan" />
          <span>Serverless Real-Time Detection Engine</span>
        </div>

        <h1 className="text-3xl sm:text-5xl lg:text-6xl font-extrabold text-white tracking-tight leading-[1.15]">
          Detect Phishing <br />
          <span className="bg-gradient-to-r from-cyber-cyan via-sky-400 to-cyber-blue bg-clip-text text-transparent">
            Before It Detects You.
          </span>
        </h1>

        <p className="mt-5 text-base sm:text-lg text-slate-300 font-normal leading-relaxed max-w-2xl mx-auto">
          Analyze suspicious websites instantly and identify potential phishing threats before entering sensitive information.
        </p>
      </div>

      {/* Interactive URL Scanner Box */}
      <div className="mt-10 max-w-3xl mx-auto">
        <div className="cyber-card rounded-2xl p-3 sm:p-4 border border-[#1E3252] shadow-2xl focus-within:border-cyber-cyan/50 transition-all">
          <form
            onSubmit={e => {
              e.preventDefault();
              handleScan();
            }}
            className="flex flex-col sm:flex-row items-center gap-3"
          >
            <div className="relative flex-1 w-full">
              <div className="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-none text-slate-400">
                <Search className="w-4 h-4 text-cyber-cyan" />
              </div>
              <input
                type="text"
                value={urlInput}
                onChange={e => {
                  setUrlInput(e.target.value);
                  if (errorMessage) {
                    setErrorMessage('');
                    setIsBackendError(false);
                  }
                }}
                placeholder="Enter URL to check (e.g. amazon-login-security.xyz or google.com)"
                className="w-full pl-10 pr-4 py-3.5 bg-[#080E1A] text-white text-sm rounded-xl border border-[#1E3252] placeholder:text-slate-500 focus:outline-none focus:border-cyber-cyan transition-colors font-mono"
              />
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full sm:w-auto px-6 py-3.5 rounded-xl bg-cyber-cyan hover:bg-cyber-cyan/90 text-slate-950 font-bold text-sm flex items-center justify-center gap-2 transition-all shadow-[0_0_20px_rgba(0,212,255,0.3)] disabled:opacity-50 disabled:cursor-not-allowed flex-shrink-0"
            >
              {loading ? (
                <>
                  <Loader2 className="w-4 h-4 animate-spin text-slate-950" />
                  <span>Analyzing...</span>
                </>
              ) : (
                <>
                  <Shield className="w-4 h-4 text-slate-950" />
                  <span>Analyze URL</span>
                </>
              )}
            </button>
          </form>

          {/* Error Message Box */}
          {errorMessage && (
            <div className="mt-3 p-3.5 rounded-xl border flex flex-col sm:flex-row sm:items-center justify-between gap-2 animate-fade-in bg-cyber-amber/10 border-cyber-amber/40 text-cyber-amber">
              <div className="flex items-start gap-2 text-xs font-mono">
                <AlertOctagon className="w-4 h-4 flex-shrink-0 mt-0.5" />
                <span>{errorMessage}</span>
              </div>
            </div>
          )}

          {/* Loading Stage Indicator */}
          {loading && (
            <div className="mt-4 p-3 rounded-xl bg-[#080E1A] border border-cyber-cyan/30 flex items-center justify-between animate-pulse">
              <div className="flex items-center gap-2.5 text-xs font-mono text-cyber-cyan">
                <Loader2 className="w-3.5 h-3.5 animate-spin" />
                <span>{loadingStep}</span>
              </div>
              <span className="text-[10px] font-mono text-slate-400">Serverless /api/analyze</span>
            </div>
          )}
        </div>

        {/* Quick Demo Preset Pills for Evaluators */}
        <div className="mt-5">
          <div className="flex items-center justify-between mb-2 px-1">
            <span className="text-xs font-mono text-slate-400 font-medium">
              Demo Preset Targets (Click to test):
            </span>
            <span className="text-[11px] font-mono text-cyber-cyan flex items-center gap-1">
              <Server className="w-3 h-3" />
              Route: POST /api/analyze
            </span>
          </div>

          <div className="flex flex-wrap gap-2">
            {DEMO_PRESETS.map((preset, index) => {
              const badgeCol =
                preset.type === 'danger'
                  ? 'border-cyber-rose/30 text-cyber-rose bg-cyber-rose/10 hover:bg-cyber-rose/20'
                  : preset.type === 'warning'
                  ? 'border-cyber-amber/30 text-cyber-amber bg-cyber-amber/10 hover:bg-cyber-amber/20'
                  : 'border-cyber-emerald/30 text-cyber-emerald bg-cyber-emerald/10 hover:bg-cyber-emerald/20';

              return (
                <button
                  key={index}
                  type="button"
                  onClick={() => handlePresetClick(preset.url)}
                  className={`text-xs font-mono px-3 py-1.5 rounded-lg border transition-all flex items-center gap-1.5 ${badgeCol}`}
                >
                  {preset.type === 'danger' && <ShieldAlert className="w-3 h-3" />}
                  {preset.type === 'warning' && <AlertTriangle className="w-3 h-3" />}
                  {preset.type === 'safe' && <CheckCircle2 className="w-3 h-3" />}
                  <span>{preset.label}</span>
                </button>
              );
            })}
          </div>
        </div>
      </div>

      {/* Render Scan Results if Available */}
      {result && <ResultCard result={result} onReset={() => setResult(null)} />}
    </section>
  );
};
