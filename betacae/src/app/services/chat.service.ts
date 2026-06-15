import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface ChatMessage {
  role: 'user' | 'assistant';
  content: string;
  timestamp: Date;
}

export interface ApiResponse {
  answer: string;
  sources?: string[];
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

  uploadDocument(file: File): Observable<{ message: string }> {
    const formData = new FormData();
    formData.append('file', file);
    return this.http.post<{ message: string }>(`${this.apiUrl}/upload`, formData);
  }
}
