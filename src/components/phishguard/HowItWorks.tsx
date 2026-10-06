'use client';

import React from 'react';
import {
  Globe,
  Layers,
  Cpu,
  Database,
  BrainCircuit,
  Gauge,
  ShieldAlert,
  ArrowRight,
  Info
} from 'lucide-react';

const PIPELINE_STEPS = [
  {
    step: '01',
    title: 'User Visits a Website',
    desc: 'The user clicks a link from email, SMS, or web navigation in the browser.',
    latency: '0 ms',
    icon: Globe,
    color: 'text-slate-300'
  },
  {
    step: '02',
    title: 'Extension Captures URL',
    desc: 'Lightweight client extension intercepts the navigation event via webNavigation APIs.',
    latency: '< 2 ms',
    icon: Layers,
    color: 'text-cyber-cyan'
  },
  {
    step: '03',
    title: 'Fast URL Analysis',
    desc: 'On-device Bloom filter checks top 50,000 safe domains + runs structural lexical heuristics.',
    latency: '< 10 ms',
    icon: Cpu,
    color: 'text-cyber-emerald'
  },
  {
    step: '04',
    title: 'Threat Intelligence Check',
    desc: 'Cached k-anonymity hash-prefix lookup against known phishing domain feeds.',
    latency: '< 60 ms',
    icon: Database,
    color: 'text-cyber-blue'
  },
  {
    step: '05',
    title: 'AI / ML Risk Analysis',
    desc: 'Zero-day classifier scores extracted DOM features, form actions, and brand similarity.',
    latency: '< 120 ms',
    icon: BrainCircuit,
    color: 'text-cyber-amber'
  },
  {
    step: '06',
    title: 'Risk Score Generated',
    desc: 'Calibrated composite risk score (0 to 100) produced with explainable indicators.',
    latency: '< 10 ms',
    icon: Gauge,
    color: 'text-sky-400'
  },
  {
    step: '07',
    title: 'User Receives Warning',
    desc: 'Safe sites proceed instantly; phishing links trigger an immediate browser blocking overlay.',
    latency: 'Instant UI',
    icon: ShieldAlert,
    color: 'text-cyber-rose'
  }
];

export const HowItWorks: React.FC = () => {
  return (
    <section id="how-it-works" className="py-20 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto border-t border-[#1E3252]/60">
      <div className="text-center max-w-3xl mx-auto mb-16">
        <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyber-card border border-cyber-border text-xs font-mono text-cyber-cyan mb-4">
          <Layers className="w-3.5 h-3.5 text-cyber-cyan" />
          <span>Multi-Layer Detection Pipeline</span>
        </div>
        <h2 className="text-2xl sm:text-4xl font-extrabold text-white tracking-tight">
          How WEBNOX Protects Every Click
        </h2>
        <p className="mt-3 text-sm sm:text-base text-slate-300">
          A progressive, multi-stage detection pipeline designed to stop zero-day threats without degrading browsing speed.
        </p>
      </div>

      {/* 7-Step Progressive Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {PIPELINE_STEPS.map((s, idx) => {
          const Icon = s.icon;
          return (
            <div
              key={idx}
              className={`cyber-card rounded-2xl p-5 border border-[#1E3252] hover:border-cyber-cyan/40 transition-all flex flex-col justify-between ${
                idx === 6 ? 'md:col-span-2 lg:col-span-2' : ''
              }`}
            >
              <div>
                <div className="flex items-center justify-between mb-4">
                  <span className="text-xs font-mono font-bold px-2 py-0.5 rounded bg-[#080E1A] text-slate-400 border border-[#1E3252]">
                    STEP {s.step}
                  </span>
                  <span className="text-[11px] font-mono text-cyber-cyan bg-cyber-cyan/10 px-2 py-0.5 rounded border border-cyber-cyan/20">
                    {s.latency}
                  </span>
                </div>

                <div className="flex items-center gap-2.5 mb-2">
                  <Icon className={`w-5 h-5 ${s.color}`} />
                  <h3 className="text-sm font-bold text-white">{s.title}</h3>
                </div>

                <p className="text-xs text-slate-400 leading-relaxed font-normal">
                  {s.desc}
                </p>
              </div>

              {idx < 6 && (
                <div className="mt-4 pt-3 border-t border-[#1E3252]/50 flex items-center justify-between text-[11px] text-slate-500 font-mono">
                  <span>Next stage</span>
                  <ArrowRight className="w-3.5 h-3.5 text-cyber-cyan" />
                </div>
              )}
            </div>
          );
        })}
      </div>
    </section>
  );
};
