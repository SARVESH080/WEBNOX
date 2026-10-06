'use client';

import React from 'react';
import {
  Layers,
  Server,
  Cpu,
  Database,
  ShieldCheck,
  CheckCircle2,
  FileCode,
  Lock
} from 'lucide-react';

export const ArchitectureSection: React.FC = () => {
  return (
    <section id="architecture" className="py-20 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto border-t border-[#1E3252]/60">
      <div className="text-center max-w-3xl mx-auto mb-16">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyber-card border border-cyber-border text-xs font-mono text-cyber-cyan mb-4">
          <Server className="w-3.5 h-3.5 text-cyber-cyan" />
          <span>Technical Architecture</span>
        </div>
        <h2 className="text-2xl sm:text-4xl font-extrabold text-white tracking-tight">
          Designed for Sub-50ms Low Latency
        </h2>
        <p className="mt-3 text-sm sm:text-base text-slate-300">
          A hybrid edge-cloud pipeline where 90%+ of legitimate web traffic exits at the browser layer without cloud delay.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Component 1: Edge Client */}
        <div className="cyber-card rounded-2xl p-6 border border-[#1E3252] hover:border-cyber-cyan/40 transition-all">
          <div className="w-10 h-10 rounded-xl bg-cyber-cyan/15 border border-cyber-cyan/30 flex items-center justify-center text-cyber-cyan mb-4">
            <Cpu className="w-5 h-5" />
          </div>
          <h3 className="text-base font-bold text-white mb-1">1. Edge Client (Extension)</h3>
          <span className="text-[11px] font-mono text-cyber-cyan">Manifest V3 • TypeScript</span>
          <p className="text-xs text-slate-400 mt-3 leading-relaxed">
            Runs directly inside Chrome/Edge. Contains an in-memory Bloom filter for the top 50,000 domains and performs instantaneous DOM inspection without network latency.
          </p>
          <ul className="mt-4 space-y-2 text-xs text-slate-300 font-mono">
            <li className="flex items-center gap-2">
              <CheckCircle2 className="w-3.5 h-3.5 text-cyber-emerald flex-shrink-0" />
              <span>O(1) Local Allowlist Check</span>
            </li>
            <li className="flex items-center gap-2">
              <CheckCircle2 className="w-3.5 h-3.5 text-cyber-emerald flex-shrink-0" />
              <span>Speculative Form Shielding</span>
            </li>
            <li className="flex items-center gap-2">
              <CheckCircle2 className="w-3.5 h-3.5 text-cyber-emerald flex-shrink-0" />
              <span>Anti-Cloaking DOM Vectors</span>
            </li>
          </ul>
        </div>

        {/* Component 2: Cloud Microservice */}
        <div className="cyber-card rounded-2xl p-6 border border-[#1E3252] hover:border-cyber-cyan/40 transition-all">
          <div className="w-10 h-10 rounded-xl bg-cyber-blue/15 border border-cyber-blue/30 flex items-center justify-center text-cyber-blue mb-4">
            <Server className="w-5 h-5" />
          </div>
          <h3 className="text-base font-bold text-white mb-1">2. Low-Latency Backend</h3>
          <span className="text-[11px] font-mono text-cyber-blue">Python • FastAPI • Redis</span>
          <p className="text-xs text-slate-400 mt-3 leading-relaxed">
            Asynchronous ASGI backend designed to score numerical feature vectors in under 10ms. No heavy crawler overhead; queries are processed in real time.
          </p>
          <ul className="mt-4 space-y-2 text-xs text-slate-300 font-mono">
            <li className="flex items-center gap-2">
              <CheckCircle2 className="w-3.5 h-3.5 text-cyber-emerald flex-shrink-0" />
              <span>Asynchronous JSON Vector API</span>
            </li>
            <li className="flex items-center gap-2">
              <CheckCircle2 className="w-3.5 h-3.5 text-cyber-emerald flex-shrink-0" />
              <span>Upstash Redis Caching</span>
            </li>
            <li className="flex items-center gap-2">
              <CheckCircle2 className="w-3.5 h-3.5 text-cyber-emerald flex-shrink-0" />
              <span>k-Anonymity SHA-256 Hash Match</span>
            </li>
          </ul>
        </div>

        {/* Component 3: Machine Learning Model */}
        <div className="cyber-card rounded-2xl p-6 border border-[#1E3252] hover:border-cyber-cyan/40 transition-all">
          <div className="w-10 h-10 rounded-xl bg-cyber-amber/15 border border-cyber-amber/30 flex items-center justify-center text-cyber-amber mb-4">
            <Database className="w-5 h-5" />
          </div>
          <h3 className="text-base font-bold text-white mb-1">3. Zero-Day ML Model</h3>
          <span className="text-[11px] font-mono text-cyber-amber">LightGBM / XGBoost Model</span>
          <p className="text-xs text-slate-400 mt-3 leading-relaxed">
            Trained on high-confidence datasets (PhishTank, OpenPhish, Tranco 1M). Classifies lexical entropy, brand similarity, and form action targets before feeds report them.
          </p>
          <ul className="mt-4 space-y-2 text-xs text-slate-300 font-mono">
            <li className="flex items-center gap-2">
              <CheckCircle2 className="w-3.5 h-3.5 text-cyber-emerald flex-shrink-0" />
              <span>Sub-5ms Inference Time</span>
            </li>
            <li className="flex items-center gap-2">
              <CheckCircle2 className="w-3.5 h-3.5 text-cyber-emerald flex-shrink-0" />
              <span>Low False Positive Optimization</span>
            </li>
            <li className="flex items-center gap-2">
              <CheckCircle2 className="w-3.5 h-3.5 text-cyber-emerald flex-shrink-0" />
              <span>Explainable Indicator Breakdown</span>
            </li>
          </ul>
        </div>
      </div>
    </section>
  );
};
