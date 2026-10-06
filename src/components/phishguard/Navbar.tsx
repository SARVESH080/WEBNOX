'use client';

import React from 'react';
import { Shield, ShieldAlert, Cpu, Sparkles } from 'lucide-react';

export const Navbar: React.FC = () => {
  return (
    <header className="sticky top-0 z-50 w-full border-b border-[#1E3252]/80 bg-[#070D18]/85 backdrop-blur-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-18 flex items-center justify-between">
        {/* Brand Logo & Name */}
        <div className="flex items-center gap-3">
          <div className="relative flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-cyber-cyan/20 to-cyber-blue/30 border border-cyber-cyan/40 shadow-[0_0_15px_rgba(0,212,255,0.25)]">
            <Shield className="w-5 h-5 text-cyber-cyan" />
            <span className="absolute -top-1 -right-1 w-2.5 h-2.5 bg-cyber-emerald rounded-full animate-ping" />
            <span className="absolute -top-1 -right-1 w-2.5 h-2.5 bg-cyber-emerald rounded-full" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="font-bold text-lg text-white tracking-tight">WEBNOX</span>
              <span className="text-[10px] font-mono px-2 py-0.5 rounded-full bg-cyber-cyan/10 border border-cyber-cyan/30 text-cyber-cyan font-semibold">
                SECURITY
              </span>
            </div>
            <p className="text-xs text-slate-400 font-medium">Real-Time Phishing Protection</p>
          </div>
        </div>

        {/* Navigation Links */}
        <nav className="hidden md:flex items-center gap-6 text-sm font-medium text-slate-300">
          <a href="#hero" className="hover:text-cyber-cyan transition-colors">
            Scanner
          </a>
          <a href="#how-it-works" className="hover:text-cyber-cyan transition-colors">
            How It Works
          </a>
        </nav>

        {/* Action / Tag */}
        <div className="flex items-center gap-3">
          <a
            href="#hero"
            className="flex items-center gap-1.5 px-3.5 py-1.5 text-xs font-semibold rounded-lg bg-cyber-cyan text-slate-950 hover:bg-cyber-cyan/90 transition-all shadow-[0_0_12px_rgba(0,212,255,0.3)]"
          >
            <Sparkles className="w-3.5 h-3.5" />
            <span>Test Demo URL</span>
          </a>
        </div>
      </div>
    </header>
  );
};
