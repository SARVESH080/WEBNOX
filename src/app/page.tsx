'use client';

import React from 'react';
import { Navbar } from '@/components/phishguard/Navbar';
import { HeroScanner } from '@/components/phishguard/HeroScanner';
import { HowItWorks } from '@/components/phishguard/HowItWorks';
import { Footer } from '@/components/phishguard/Footer';

export default function Home() {
  return (
    <div className="min-h-screen bg-[#070D18] flex flex-col relative overflow-x-hidden">
      {/* Background Matrix/Subtle Grid Texture */}
      <div className="fixed inset-0 bg-grid-cyber pointer-events-none -z-20 opacity-40" />

      {/* Navigation Header */}
      <Navbar />

      {/* Main Content Area */}
      <main className="flex-1 w-full">
        {/* Hero Section with Interactive Live Scanner */}
        <HeroScanner />

        {/* 7-Stage How It Works Flow */}
        <HowItWorks />
      </main>

      {/* Professional Cybersecurity Footer */}
      <Footer />
    </div>
  );
}
