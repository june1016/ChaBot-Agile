import { NextResponse } from 'next/server';
import axios from 'axios';

export async function POST(request: Request) {
  const { input } = await request.json();

  try {
    const response = await axios.post('http://localhost:8000/query', { input });
    return NextResponse.json(response.data);
  } catch (error) {
    console.error('Error querying the chatbot:', error);
    return NextResponse.json(
      { error: 'An error occurred while processing your request' },
      { status: 500 }
    );
  }
}
