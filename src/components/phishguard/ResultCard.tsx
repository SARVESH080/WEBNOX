'use client';

import React, { useState } from 'react';
import {
  ShieldCheck,
  ShieldAlert,
  AlertTriangle,
  Clock,
  Globe,
  RotateCcw,
  CheckCircle2,
  XCircle,
  HelpCircle,
  Layers,
  ArrowRight,
  Sparkles,
  Shield
} from 'lucide-react';
import { BackendAnalyzeResponse } from '@/lib/api';

export interface DisplayResult extends BackendAnalyzeResponse {
  latencyMs: number;
  timestamp: string;
  protocol: string;
  hostname: string;
  pathname: string;
}

interface ResultCardProps {
  result: DisplayResult;
  onReset: () => void;
}

export const ResultCard: React.FC<ResultCardProps> = ({ result, onReset }) => {
  const [showSimulatedModal, setShowSimulatedModal] = useState(false);

  const isSafe = result.verdict === 'safe';
  const isSuspicious = result.verdict === 'suspicious';
  const isPhishing = result.verdict === 'phishing';

  // Dynamic visual styles
  const statusColor = isSafe
    ? 'text-cyber-emerald'
    : isSuspicious
    ? 'text-cyber-amber'
    : 'text-cyber-rose';

  const statusBg = isSafe
    ? 'bg-cyber-emerald/10 border-cyber-emerald/30'
    : isSuspicious
    ? 'bg-cyber-amber/10 border-cyber-amber/30'
    : 'bg-cyber-rose/10 border-cyber-rose/30';

  const cardGlowClass = isSafe
    ? 'cyber-glow-emerald'
    : isSuspicious
    ? 'cyber-glow-amber'
    : 'cyber-glow-red';

  const StatusIcon = isSafe
    ? ShieldCheck
    : isSuspicious
    ? AlertTriangle
    : ShieldAlert;

  const displayStatus = isSafe ? 'SAFE' : isSuspicious ? 'SUSPICIOUS' : 'PHISHING';

  return (
    <div className="w-full max-w-4xl mx-auto mt-8 animate-fade-in transition-all">
      {/* Main Analysis Card */}
      <div className={`cyber-card rounded-2xl p-6 sm:p-8 ${cardGlowClass} transition-all`}>
        {/* Top Header Row */}
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 pb-6 border-b border-[#1E3252]">
          <div className="flex items-center gap-3.5">
            <div className={`p-3 rounded-xl border ${statusBg}`}>
              <StatusIcon className={`w-8 h-8 ${statusColor}`} />
            </div>
            <div>
              <div className="flex items-center gap-2 flex-wrap">
                <span className={`text-xs font-mono font-bold tracking-wider uppercase px-2.5 py-0.5 rounded-full border ${statusBg} ${statusColor}`}>
                  {displayStatus}
                </span>
                <span className="text-xs font-mono text-slate-400 flex items-center gap-1">
                  <Clock className="w-3.5 h-3.5 text-cyber-cyan" />
                  {result.latencyMs} ms API latency
                </span>
                <span className="text-[11px] font-mono px-2 py-0.5 rounded bg-[#0F1A2E] text-cyber-cyan border border-[#1E3252]">
                  {result.confidence}% Confidence
                </span>
              </div>
              <h2 className="text-xl sm:text-2xl font-bold text-white mt-1">
                {isSafe && 'Safe Website Verified'}
                {isSuspicious && 'Suspicious Website Warning'}
                {isPhishing && 'Phishing Attack Detected'}
              </h2>
            </div>
          </div>

          {/* Risk Score Pill Gauge */}
          <div className="flex items-center gap-3 bg-[#080E1A] px-4 py-2.5 rounded-xl border border-[#1E3252] self-stretch sm:self-auto justify-between sm:justify-start">
            <div className="text-right">
              <div className="text-[11px] font-mono uppercase text-slate-400">Risk Assessment</div>
              <div className="text-xs text-slate-300 font-medium">
                {isSafe ? 'Low Threat (0-30)' : isSuspicious ? 'Medium Threat (31-60)' : 'High Threat (61-100)'}
              </div>
            </div>
            <div className="relative flex items-center justify-center w-14 h-14 rounded-full bg-[#0F1A2E] border-2 border-[#1E3252]">
              <span className={`text-lg font-bold font-mono ${statusColor}`}>
                {result.risk_score}
              </span>
              <span className="text-[9px] text-slate-400 absolute bottom-1">/100</span>
            </div>
          </div>
        </div>

        {/* Analyzed URL Banner */}
        <div className="mt-6 p-4 rounded-xl bg-[#080E1A]/80 border border-[#1E3252] flex flex-col md:flex-row md:items-center justify-between gap-3">
          <div className="flex items-center gap-2.5 overflow-hidden">
            <Globe className="w-4 h-4 text-cyber-cyan flex-shrink-0" />
            <div className="text-xs font-mono truncate text-slate-300">
              <span className="text-slate-500">{result.protocol}://</span>
              <span className="text-white font-semibold">{result.hostname}</span>
              <span className="text-slate-400">{result.pathname}</span>
            </div>
          </div>

          <div className="flex items-center gap-2 flex-shrink-0">
            <span className="text-[11px] font-mono px-2 py-0.5 rounded bg-[#0F1A2E] text-slate-400 border border-[#1E3252]">
              TLD: .{result.hostname.split('.').pop()}
            </span>
            <span className="text-[11px] font-mono px-2 py-0.5 rounded bg-[#0F1A2E] text-slate-400 border border-[#1E3252]">
              Engine: Serverless Rule-Based
            </span>
          </div>
        </div>

        {/* Recommendation Box */}
        <div className={`mt-4 p-3.5 rounded-xl border ${statusBg} flex items-start gap-2.5`}>
          <StatusIcon className={`w-4 h-4 flex-shrink-0 mt-0.5 ${statusColor}`} />
          <div>
            <div className={`text-xs font-bold uppercase tracking-wider ${statusColor}`}>
              Recommendation
            </div>
            <p className="text-xs text-slate-200 mt-0.5 leading-relaxed">
              {result.recommendation}
            </p>
          </div>
        </div>

        {/* Detection Reasons List */}
        <div className="mt-6">
          <h3 className="text-xs font-mono font-bold uppercase tracking-wider text-slate-400 mb-3 flex items-center gap-1.5">
            <Layers className="w-4 h-4 text-cyber-cyan" />
            Specific Reasons Identified by Detection Engine ({result.reasons.length})
          </h3>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            {result.reasons.map((reason, idx) => (
              <div
                key={idx}
                className="p-3.5 rounded-xl bg-[#080E1A]/60 border border-[#1E3252]/80 hover:border-[#1E3252] transition-colors"
              >
                <div className="flex items-start gap-2.5">
                  {isSafe ? (
                    <CheckCircle2 className="w-4 h-4 text-cyber-emerald flex-shrink-0 mt-0.5" />
                  ) : isSuspicious ? (
                    <AlertTriangle className="w-4 h-4 text-cyber-amber flex-shrink-0 mt-0.5" />
                  ) : (
                    <XCircle className="w-4 h-4 text-cyber-rose flex-shrink-0 mt-0.5" />
                  )}
                  <div>
                    <h4 className="text-xs font-semibold text-white">{reason}</h4>
                    <p className="text-[11px] text-slate-400 mt-0.5 leading-snug">
                      Rule evaluation factor from serverless engine
                    </p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Action Buttons */}
        <div className="mt-8 pt-6 border-t border-[#1E3252] flex flex-col sm:flex-row items-center justify-between gap-4">
          <button
            onClick={onReset}
            className="w-full sm:w-auto flex items-center justify-center gap-2 px-5 py-2.5 rounded-xl bg-[#0F1A2E] hover:bg-[#14233D] text-white text-xs font-semibold border border-[#1E3252] transition-all"
          >
            <RotateCcw className="w-3.5 h-3.5 text-cyber-cyan" />
            Analyze Another URL
          </button>

          <div className="flex items-center gap-3 w-full sm:w-auto">
            <button
              onClick={() => setShowSimulatedModal(!showSimulatedModal)}
              className={`w-full sm:w-auto flex items-center justify-center gap-1.5 px-4 py-2.5 rounded-xl text-xs font-semibold border transition-all ${
                isPhishing
                  ? 'bg-cyber-rose/20 text-cyber-rose border-cyber-rose/40 hover:bg-cyber-rose/30'
                  : 'bg-cyber-cyan/15 text-cyber-cyan border-cyber-cyan/30 hover:bg-cyber-cyan/25'
              }`}
            >
              <span>Simulate Browser Warning</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </button>
          </div>
        </div>

        {/* Backend Verification Notice */}
        <div className="mt-6 pt-4 border-t border-[#1E3252]/50 flex items-center justify-between text-[11px] text-slate-500 font-mono">
          <div className="flex items-center gap-2">
            <HelpCircle className="w-3.5 h-3.5 text-slate-400 flex-shrink-0" />
            <span>
              Real-time analysis from Serverless Route (<code className="text-cyber-cyan">POST /api/analyze</code>).
            </span>
          </div>
          <span className="hidden sm:inline text-slate-400">
            Next.js Serverless API
          </span>
        </div>
      </div>

      {/* Simulated Browser Interception Modal */}
      {showSimulatedModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm p-4 animate-fade-in">
          <div className="max-w-lg w-full bg-[#0F1A2E] rounded-2xl border border-cyber-border shadow-2xl p-6 sm:p-7 relative">
            <div className="flex items-center gap-3 mb-4">
              <div className={`p-2.5 rounded-xl border ${statusBg}`}>
                <StatusIcon className={`w-6 h-6 ${statusColor}`} />
              </div>
              <div>
                <span className="text-[10px] font-mono text-slate-400 uppercase tracking-widest">
                  WEBNOX Browser Shield
                </span>
                <h3 className="text-lg font-bold text-white">
                  {isPhishing && '🚨 PHISHING WEBSITE BLOCKED'}
                  {isSuspicious && '⚠️ CAUTION: SUSPICIOUS WEBSITE'}
                  {isSafe && '✅ VERIFIED SAFE WEBSITE'}
                </h3>
              </div>
            </div>

            <div className="p-3 rounded-lg bg-[#080E1A] border border-[#1E3252] text-xs font-mono text-slate-300 break-all mb-4">
              {result.url}
            </div>

            <p className="text-xs text-slate-300 leading-relaxed mb-4">
              {result.recommendation}
            </p>

            <div className="space-y-1.5 mb-6 text-xs text-slate-400 font-mono">
              <div>• Risk Score: <span className={statusColor}>{result.risk_score}/100</span></div>
              <div>• Verdict: <span className={statusColor}>{displayStatus}</span></div>
              <div>• Confidence: <span className="text-cyber-cyan">{result.confidence}%</span></div>
              <div>• Detection Latency: <span className="text-cyber-cyan">{result.latencyMs} ms</span></div>
            </div>

            <div className="flex items-center justify-end gap-3">
              <button
                onClick={() => setShowSimulatedModal(false)}
                className="px-4 py-2 rounded-xl bg-[#080E1A] hover:bg-[#14233D] text-xs font-semibold text-slate-300 border border-[#1E3252]"
              >
                Close Preview
              </button>
              {isPhishing && (
                <button
                  onClick={() => setShowSimulatedModal(false)}
                  className="px-4 py-2 rounded-xl bg-cyber-rose text-white text-xs font-bold hover:bg-cyber-rose/90 shadow-[0_0_12px_rgba(239,68,68,0.4)]"
                >
                  LEAVE WEBSITE
                </button>
              )}
              {isSuspicious && (
                <button
                  onClick={() => setShowSimulatedModal(false)}
                  className="px-4 py-2 rounded-xl bg-cyber-amber text-slate-950 text-xs font-bold hover:bg-cyber-amber/90"
                >
                  PROCEED WITH CAUTION
                </button>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
