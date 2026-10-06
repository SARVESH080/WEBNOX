import type { Metadata, Viewport } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'WEBNOX — Real-Time Phishing Detection',
  description: 'Fast, real-time phishing detection engine powered by FastAPI and rule-based risk analysis.',
  keywords: ['WEBNOX', 'Phishing Detection', 'Cybersecurity', 'URL Security', 'FastAPI'],
  authors: [{ name: 'Team WEBNOX' }],
};

export const viewport: Viewport = {
  width: 'device-width',
  initialScale: 1,
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="dark scroll-smooth">
      <body className="min-h-screen bg-[#070D18] text-slate-100 font-sans antialiased selection:bg-cyan-500 selection:text-slate-950">
        {children}
      </body>
    </html>
  );
}
