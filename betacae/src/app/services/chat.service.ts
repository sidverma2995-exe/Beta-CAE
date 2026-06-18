import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface ChatMessage {
  role: 'user' | 'assistant';
  content: string;
  timestamp: Date;
  chunks?: Array<{ source: string; content: string }>;
}

export interface ApiResponse {
  answer: string;
  sources?: string[];
  chunks?: Array<{ source: string; content: string }>;
}

export interface StreamEvent {
  token?: string;
  done?: boolean;
  sources?: string[];
  chunks?: Array<{ source: string; content: string }>;
  error?: string;
}

@Injectable({
  providedIn: 'root'
})
export class ChatService {
  private apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) {}

  askQuestion(query: string, mode: 'qa' | 'chat' | 'code'): Observable<ApiResponse> {
    return this.http.post<ApiResponse>(`${this.apiUrl}/query`, { query, mode });
  }

  streamQuery(query: string, mode: 'qa' | 'chat' | 'code'): Observable<StreamEvent> {
    return new Observable(observer => {
      fetch(`${this.apiUrl}/query/stream`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query, mode }),
      }).then(async response => {
        if (!response.ok) {
          observer.error(new Error(`HTTP error ${response.status}`));
          return;
        }
        const reader = response.body!.getReader();
        const decoder = new TextDecoder();
        let buffer = '';

        while (true) {
          const { done, value } = await reader.read();
          if (done) break;

          buffer += decoder.decode(value, { stream: true });
          const lines = buffer.split('\n');
          buffer = lines.pop() ?? '';

          for (const line of lines) {
            if (line.startsWith('data: ')) {
              try {
                const event: StreamEvent = JSON.parse(line.slice(6));
                observer.next(event);
                if (event.done || event.error) {
                  observer.complete();
                  return;
                }
              } catch {}
            }
          }
        }
        observer.complete();
      }).catch(err => observer.error(err));
    });
  }

  uploadDocument(file: File): Observable<{ message: string }> {
    const formData = new FormData();
    formData.append('file', file);
    return this.http.post<{ message: string }>(`${this.apiUrl}/upload`, formData);
  }
}
