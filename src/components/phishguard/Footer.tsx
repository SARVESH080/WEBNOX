'use client';

import React from 'react';
import { Shield, Lock, Terminal, Cpu } from 'lucide-react';

export const Footer: React.FC = () => {
  return (
    <footer className="w-full border-t border-[#1E3252]/80 bg-[#070D18] py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-6">
        <div className="flex items-center gap-3">
          <div className="flex items-center justify-center w-8 h-8 rounded-lg bg-cyber-cyan/15 border border-cyber-cyan/30">
            <Shield className="w-4 h-4 text-cyber-cyan" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="font-bold text-sm text-white">WEBNOX</span>
              <span className="text-[10px] font-mono text-slate-400">Security Suite</span>
            </div>
            <p className="text-xs text-slate-500">Real-Time Progressive Phishing Detection Engine</p>
          </div>
        </div>

        <div className="text-center md:text-right text-xs text-slate-400 space-y-1">
          <p>Real-Time Phishing Protection & Threat Analysis</p>
          <p className="text-slate-500 font-mono text-[11px]">
            FastAPI Rule-Based Detection Microservice & Interactive Dashboard
          </p>
        </div>
      </div>
    </footer>
  );
};
