import { NextRequest, NextResponse } from 'next/server';
import { analyzeUrl } from '@/lib/detector';

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();
    const targetUrl = body?.url?.trim();

    if (!targetUrl) {
      return NextResponse.json(
        { detail: 'URL cannot be empty' },
        { status: 400 }
      );
    }

    // If the backend service binding is available (e.g., in Vercel Services via BACKEND_URL),
    // route the analysis request internally to the backend FastAPI service.
    if (process.env.BACKEND_URL) {
      try {
        const backendEndpoint = new URL('/analyze', process.env.BACKEND_URL);
        const backendRes = await fetch(backendEndpoint, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ url: targetUrl }),
        });

        if (!backendRes.ok) {
          const errorData = await backendRes.json().catch(() => ({}));
          return NextResponse.json(
            { detail: errorData.detail || `Backend error (${backendRes.status})` },
            { status: backendRes.status }
          );
        }

        const data = await backendRes.json();
        return NextResponse.json(data, { status: 200 });
      } catch (err: any) {
        console.warn('Backend service call failed, falling back to local detector:', err?.message);
      }
    }

    const result = analyzeUrl(targetUrl);
    return NextResponse.json(result, { status: 200 });
  } catch (error: any) {
    return NextResponse.json(
      { detail: error?.message || 'Invalid request body' },
      { status: 400 }
    );
  }
}

export async function GET() {
  return NextResponse.json({
    status: 'online',
    service: 'WEBNOX Serverless Phishing Detection API',
    endpoint: 'POST /api/analyze',
    backendBindingConfigured: Boolean(process.env.BACKEND_URL),
  });
}
