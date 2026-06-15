import { Component } from '@angular/core';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';
import { ChatService } from './services/chat.service';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, RouterLink, RouterLinkActive],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  title = 'Beta CAE';
  uploadMessage = '';
  isUploading = false;

  constructor(private chatService: ChatService) {}

  onUploadClick() {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = '.txt,.md,.py,.js,.ts,.html,.css,.pdf';
    input.onchange = (event: Event) => {
      const file = (event.target as HTMLInputElement).files?.[0];
      if (file) {
        this.isUploading = true;
        this.uploadMessage = '';
        this.chatService.uploadDocument(file).subscribe({
          next: (res) => {
            this.uploadMessage = res.message;
            this.isUploading = false;
            setTimeout(() => this.uploadMessage = '', 4000);
          },
          error: () => {
            this.uploadMessage = 'Upload failed. Please try again.';
            this.isUploading = false;
            setTimeout(() => this.uploadMessage = '', 4000);
          }
        });
      }
    };
    input.click();
  }
}
