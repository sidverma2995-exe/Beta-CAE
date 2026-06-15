import { Routes } from '@angular/router';
import { QaComponent } from './components/qa/qa.component';
import { ChatComponent } from './components/chat/chat.component';
import { CodeComponent } from './components/code/code.component';

export const routes: Routes = [
  { path: '', redirectTo: '/qa', pathMatch: 'full' },
  { path: 'qa', component: QaComponent },
  { path: 'chat', component: ChatComponent },
  { path: 'code', component: CodeComponent },
];
