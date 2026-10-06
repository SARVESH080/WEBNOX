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
  });
}
