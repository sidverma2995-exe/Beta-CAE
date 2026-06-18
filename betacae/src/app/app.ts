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
  title = 'BTI - Dev Catalyst';
  uploadMessage = '';
  uploadStatusMessage = '';
  isUploading = false;
  uploadProgress = 0;
  uploadFileIndex = 0;   // 1-based current file number
  uploadFileTotal = 0;   // total files selected

  private apiUrl = 'http://localhost:8000';

  constructor(private chatService: ChatService) {}

  onUploadClick() {
    const input = document.createElement('input');
    input.type = 'file';
    input.multiple = true;
    input.accept = '.txt,.md,.py,.js,.ts,.html,.css,.pdf';
    input.onchange = (event: Event) => {
      const files = Array.from((event.target as HTMLInputElement).files ?? []);
      if (files.length > 0) this._uploadQueue(files);
    };
    input.click();
  }

  private async _uploadQueue(files: File[]) {
    this.isUploading = true;
    this.uploadMessage = '';
    this.uploadFileTotal = files.length;
    this.uploadFileIndex = 0;

    const succeeded: string[] = [];
    const failed: string[] = [];

    for (let i = 0; i < files.length; i++) {
      this.uploadFileIndex = i + 1;
      this.uploadProgress = 0;
      try {
        await this._uploadWithProgress(files[i]);
        succeeded.push(files[i].name);
      } catch (err: any) {
        failed.push(files[i].name);
      }
    }

    this.isUploading = false;
    this.uploadProgress = 0;

    if (failed.length === 0) {
      this.uploadMessage = files.length === 1
        ? `'${succeeded[0]}' indexed successfully.`
        : `${succeeded.length} file(s) indexed successfully.`;
    } else {
      this.uploadMessage = `${succeeded.length} succeeded, ${failed.length} failed: ${failed.join(', ')}`;
    }
    setTimeout(() => { this.uploadMessage = ''; this.uploadStatusMessage = ''; }, 6000);
  }

  private _uploadWithProgress(file: File): Promise<void> {
    this.uploadStatusMessage = `Reading '${file.name}'...`;
    const formData = new FormData();
    formData.append('file', file);

    return fetch(`${this.apiUrl}/upload/progress`, { method: 'POST', body: formData })
      .then(async response => {
        if (!response.ok) {
          const err = await response.json().catch(() => ({ detail: 'Upload failed' }));
          throw new Error(err.detail ?? 'Upload failed');
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
            if (!line.startsWith('data: ')) continue;
            try {
              const evt = JSON.parse(line.slice(6));
              const fileLabel = this.uploadFileTotal > 1
                ? `[${this.uploadFileIndex}/${this.uploadFileTotal}] `
                : '';
              this.uploadStatusMessage = fileLabel + (evt.message ?? '');

              if (evt.step === 'embedding') {
                const embPct = evt.total > 0 ? (evt.current / evt.total) * 80 : 0;
                this.uploadProgress = Math.round(10 + embPct);
              } else if (evt.step === 'parsing') {
                this.uploadProgress = 5;
              } else if (evt.step === 'chunking') {
                this.uploadProgress = evt.current > 0 ? 10 : 7;
              } else if (evt.step === 'saving') {
                this.uploadProgress = 92;
              } else if (evt.step === 'done') {
                this.uploadProgress = 100;
              } else if (evt.step === 'error') {
                throw new Error(evt.message);
              }
            } catch (parseErr: any) {
              if (parseErr?.message) throw parseErr;
            }
          }
        }
      });
  }
}
