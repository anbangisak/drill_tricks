import { Component, OnInit } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.sass'],
})
export class AppComponent implements OnInit {
  title = 'disply';

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.turnover();
  }

  turnover(){
    console.log('fade out');
    this.apiService.turnover_by_day().subscribe(
      data => {
        console.log('login success', data);
      },
      error => {
        console.error('Error saving!');
      }
    );
  }
}
