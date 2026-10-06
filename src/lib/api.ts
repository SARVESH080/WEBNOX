/**
 * API client to connect the Next.js frontend with the Next.js /api/analyze serverless route.
 * Works seamlessly both locally on localhost:3000 and when deployed to Vercel.
 */

export interface BackendAnalyzeRequest {
  url: string;
}

export interface BackendAnalyzeResponse {
  url: string;
  risk_score: number;
  verdict: 'safe' | 'suspicious' | 'phishing';
  confidence: number;
  reasons: string[];
  recommendation: string;
}

export const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || '/api';

export async function analyzeUrlWithBackend(url: string): Promise<BackendAnalyzeResponse> {
  const endpoint = `${API_BASE_URL}/analyze`.replace(/\/+/g, '/').replace(':/', '://');
  const response = await fetch(endpoint, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ url }),
  });

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    throw new Error(errorData.detail || `Server error (${response.status})`);
  }

  return response.json();
}
