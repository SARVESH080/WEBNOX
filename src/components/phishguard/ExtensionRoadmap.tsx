'use client';

import React, { useState } from 'react';
import {
  Chrome,
  Shield,
  ShieldCheck,
  ShieldAlert,
  ArrowRight,
  CheckCircle2,
  Sparkles,
  Zap,
  Lock,
  Layers,
  Sliders,
  ExternalLink
} from 'lucide-react';

export const ExtensionRoadmap: React.FC = () => {
  const [extensionEnabled, setExtensionEnabled] = useState(true);
  const [waitlistModal, setWaitlistModal] = useState(false);
  const [emailInput, setEmailInput] = useState('');
  const [emailSubmitted, setEmailSubmitted] = useState(false);

  const ROADMAP_FLOW = [
    { title: 'Web Prototype', desc: 'Current phase: Interactive UI & heuristic validation', status: 'completed' },
    { title: 'Detection Engine', desc: 'FastAPI microservice & lightweight ML zero-day model', status: 'next' },
    { title: 'Chrome Extension', desc: 'Manifest V3 client with on-device Bloom filter', status: 'upcoming' },
    { title: 'Automatic URL Detection', desc: 'Zero-touch navigation interception on every tab', status: 'upcoming' },
    { title: 'Real-Time Protection', desc: 'Full-spectrum protection against active phishing kits', status: 'upcoming' }
  ];

  return (
    <section id="extension" className="py-20 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto border-t border-[#1E3252]/60">
      <div className="text-center max-w-3xl mx-auto mb-16">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyber-card border border-cyber-border text-xs font-mono text-cyber-cyan mb-4">
          <Chrome className="w-3.5 h-3.5 text-cyber-cyan" />
          <span>Product Evolution Roadmap</span>
        </div>
        <h2 className="text-2xl sm:text-4xl font-extrabold text-white tracking-tight">
          From Web Prototype to Browser Protection
        </h2>
        <p className="mt-3 text-sm sm:text-base text-slate-300">
          The prototype demonstrates our progressive logic. Here is how it translates into automatic, background browser security.
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        {/* Left Column: Visual Step Progression Flow */}
        <div className="lg:col-span-6 space-y-3.5">
          {ROADMAP_FLOW.map((item, idx) => (
            <div
              key={idx}
              className={`cyber-card rounded-xl p-4 border transition-all flex items-center justify-between ${
                item.status === 'completed'
                  ? 'border-cyber-cyan/40 bg-cyber-cyan/5 shadow-[0_0_15px_rgba(0,212,255,0.08)]'
                  : item.status === 'next'
                  ? 'border-cyber-amber/40 bg-cyber-amber/5'
                  : 'border-[#1E3252]'
              }`}
            >
              <div className="flex items-center gap-3.5">
                <div
                  className={`w-7 h-7 rounded-lg flex items-center justify-center font-mono text-xs font-bold ${
                    item.status === 'completed'
                      ? 'bg-cyber-cyan text-slate-950'
                      : item.status === 'next'
                      ? 'bg-cyber-amber text-slate-950'
                      : 'bg-[#080E1A] text-slate-400 border border-[#1E3252]'
                  }`}
                >
                  {idx + 1}
                </div>
                <div>
                  <h4 className="text-sm font-bold text-white flex items-center gap-2">
                    {item.title}
                    {item.status === 'completed' && (
                      <span className="text-[10px] font-mono px-2 py-0.2 rounded-full bg-cyber-cyan/15 text-cyber-cyan border border-cyber-cyan/30">
                        Current
                      </span>
                    )}
                  </h4>
                  <p className="text-xs text-slate-400 mt-0.5">{item.desc}</p>
                </div>
              </div>

              {item.status === 'completed' && (
                <CheckCircle2 className="w-5 h-5 text-cyber-cyan flex-shrink-0" />
              )}
            </div>
          ))}

          <div className="pt-4">
            <button
              onClick={() => setWaitlistModal(true)}
              className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-xl bg-gradient-to-r from-cyber-cyan to-sky-400 hover:opacity-95 text-slate-950 font-bold text-sm shadow-[0_0_20px_rgba(0,212,255,0.3)] transition-all"
            >
              <Chrome className="w-4 h-4" />
              <span>Coming Soon: Chrome Extension</span>
            </button>
          </div>
        </div>

        {/* Right Column: Interactive Browser Extension Preview Mockup */}
        <div className="lg:col-span-6 flex justify-center">
          <div className="w-full max-w-sm rounded-2xl bg-[#0F1A2E] border border-cyber-border shadow-2xl p-5 relative overflow-hidden">
            {/* Top Chrome Extension Bar Mockup */}
            <div className="flex items-center justify-between pb-4 border-b border-[#1E3252] mb-4">
              <div className="flex items-center gap-2">
                <div className="w-7 h-7 rounded-lg bg-cyber-cyan/20 border border-cyber-cyan/40 flex items-center justify-center">
                  <Shield className="w-4 h-4 text-cyber-cyan" />
                </div>
                <div>
                  <h5 className="text-xs font-bold text-white">PhishGuard Extension</h5>
                  <p className="text-[10px] text-slate-400 font-mono">v1.0.0-rc (Manifest V3)</p>
                </div>
              </div>

              {/* Active Toggle Switch */}
              <button
                onClick={() => setExtensionEnabled(!extensionEnabled)}
                className={`w-11 h-6 rounded-full transition-colors relative p-0.5 ${
                  extensionEnabled ? 'bg-cyber-cyan' : 'bg-slate-700'
                }`}
              >
                <div
                  className={`w-5 h-5 rounded-full bg-slate-950 transition-transform ${
                    extensionEnabled ? 'translate-x-5' : 'translate-x-0'
                  }`}
                />
              </button>
            </div>

            {/* Current Tab Status */}
            <div className="p-3.5 rounded-xl bg-[#080E1A] border border-[#1E3252] mb-4">
              <div className="flex items-center justify-between text-[11px] font-mono text-slate-400 mb-1">
                <span>ACTIVE BROWSER TAB</span>
                <span className="text-cyber-emerald flex items-center gap-1">
                  <span className="w-1.5 h-1.5 bg-cyber-emerald rounded-full animate-ping" />
                  PROTECTED
                </span>
              </div>
              <div className="text-xs font-mono font-medium text-white truncate">
                https://mybank-online.example.com
              </div>
              <div className="mt-2 flex items-center justify-between text-[11px] text-slate-400">
                <span>Inspection Latency:</span>
                <span className="text-cyber-cyan font-mono font-bold">14 ms (Local)</span>
              </div>
            </div>

            {/* Simulated Live Protection Metrics */}
            <div className="grid grid-cols-2 gap-2.5 mb-4 text-center">
              <div className="p-2.5 rounded-lg bg-[#080E1A] border border-[#1E3252]">
                <div className="text-[10px] font-mono text-slate-400 uppercase">Threats Blocked</div>
                <div className="text-base font-bold text-cyber-rose font-mono mt-0.5">142</div>
              </div>
              <div className="p-2.5 rounded-lg bg-[#080E1A] border border-[#1E3252]">
                <div className="text-[10px] font-mono text-slate-400 uppercase">Avg Response</div>
                <div className="text-base font-bold text-cyber-cyan font-mono mt-0.5">18 ms</div>
              </div>
            </div>

            <div className="space-y-2 text-xs text-slate-300">
              <div className="flex items-center justify-between py-1 border-b border-[#1E3252]/50">
                <span className="flex items-center gap-1.5 text-slate-400">
                  <Lock className="w-3 h-3 text-cyber-emerald" />
                  Speculative Form Shielding
                </span>
                <span className="text-cyber-emerald font-mono font-semibold">Active</span>
              </div>
              <div className="flex items-center justify-between py-1 border-b border-[#1E3252]/50">
                <span className="flex items-center gap-1.5 text-slate-400">
                  <Zap className="w-3 h-3 text-cyber-cyan" />
                  Top 50k Bloom Filter
                </span>
                <span className="text-cyber-cyan font-mono font-semibold">Ready</span>
              </div>
            </div>

            {/* Extension Footer Tag */}
            <div className="mt-4 pt-3 border-t border-[#1E3252] text-center">
              <span className="text-[11px] font-mono text-slate-500">
                Simulated Extension Interface for Chrome / Edge
              </span>
            </div>
          </div>
        </div>
      </div>

      {/* Modal: Extension Waitlist / Notification */}
      {waitlistModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm p-4 animate-fade-in">
          <div className="max-w-md w-full bg-[#0F1A2E] rounded-2xl border border-cyber-border shadow-2xl p-6 sm:p-7 relative">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 rounded-xl bg-cyber-cyan/20 border border-cyber-cyan/40 flex items-center justify-center">
                <Chrome className="w-5 h-5 text-cyber-cyan" />
              </div>
              <div>
                <h3 className="text-base font-bold text-white">PhishGuard Extension Release</h3>
                <p className="text-xs text-slate-400">Manifest V3 Chrome / Edge Edition</p>
              </div>
            </div>

            {emailSubmitted ? (
              <div className="p-4 rounded-xl bg-cyber-emerald/10 border border-cyber-emerald/30 text-center space-y-2 mb-4">
                <CheckCircle2 className="w-8 h-8 text-cyber-emerald mx-auto" />
                <h4 className="text-sm font-bold text-white">You are on the preview list!</h4>
                <p className="text-xs text-slate-300">
                  We will notify you when the Chrome Web Store extension and FastAPI microservice are published.
                </p>
              </div>
            ) : (
              <form
                onSubmit={e => {
                  e.preventDefault();
                  if (emailInput) setEmailSubmitted(true);
                }}
                className="space-y-3 mb-4"
              >
                <p className="text-xs text-slate-300 leading-relaxed">
                  The extension is currently in active development for the hackathon deployment phase. Leave your email to receive early testing access.
                </p>
                <input
                  type="email"
                  required
                  value={emailInput}
                  onChange={e => setEmailInput(e.target.value)}
                  placeholder="name@university.edu or organization"
                  className="w-full px-3.5 py-2.5 bg-[#080E1A] text-white text-xs rounded-xl border border-[#1E3252] placeholder:text-slate-500 focus:outline-none focus:border-cyber-cyan font-mono"
                />
                <button
                  type="submit"
                  className="w-full py-2.5 rounded-xl bg-cyber-cyan text-slate-950 font-bold text-xs hover:bg-cyber-cyan/90 transition-all shadow-[0_0_12px_rgba(0,212,255,0.3)]"
                >
                  Join Extension Preview List
                </button>
              </form>
            )}

            <div className="flex justify-end">
              <button
                onClick={() => {
                  setWaitlistModal(false);
                  setEmailSubmitted(false);
                }}
                className="text-xs text-slate-400 hover:text-white px-3 py-1 font-mono"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}
    </section>
  );
};
