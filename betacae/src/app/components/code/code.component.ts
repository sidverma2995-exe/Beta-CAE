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

    this.chatService.askQuestion(query, 'code').subscribe({
      next: (response) => {
        this.messages.push({
          role: 'assistant',
          content: response.answer,
          timestamp: new Date()
        });
        this.isLoading = false;
      },
      error: (err) => {
        this.messages.push({
          role: 'assistant',
          content: 'Sorry, something went wrong. Please try again.',
          timestamp: new Date()
        });
        this.isLoading = false;
      }
    });
  }
}
