import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { ChatService, ChatMessage } from '../../services/chat.service';

@Component({
  selector: 'app-code',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './code.component.html',
  styleUrl: './code.component.css'
})
export class CodeComponent {
  messages: ChatMessage[] = [];
  userInput = '';
  isLoading = false;

  constructor(private chatService: ChatService) {}

  sendMessage() {
    if (!this.userInput.trim()) return;

    const userMsg: ChatMessage = {
      role: 'user',
      content: this.userInput,
      timestamp: new Date()
    };
    this.messages.push(userMsg);
    const query = this.userInput;
    this.userInput = '';
    this.isLoading = true;

    const assistantMsg: ChatMessage = { role: 'assistant', content: '', timestamp: new Date() };
    this.messages.push(assistantMsg);
    const idx = this.messages.length - 1;

    this.chatService.streamQuery(query, 'code').subscribe({
      next: (event) => {
        if (event.token) {
          this.messages[idx].content += event.token;
        }
        if (event.done) {
          this.messages[idx].chunks = event.chunks ?? [];
          this.isLoading = false;
        }
        if (event.error) {
          this.messages[idx].content = 'Sorry, something went wrong. Please try again.';
          this.isLoading = false;
        }
      },
      error: () => {
        this.messages[idx].content = 'Sorry, something went wrong. Please try again.';
        this.isLoading = false;
      },
      complete: () => { this.isLoading = false; }
    });
  }
}
