import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PreditorComponent } from './preditor/preditor.component';

const routes: Routes = [
  { path: 'preditor', component: PreditorComponent },
  { path: '**', redirectTo: 'preditor' } 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
