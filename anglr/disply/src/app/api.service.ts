import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

constructor(private http: HttpClient) { }

  public turnover_by_day() {
    console.log('coming in');
    return this.http.get('http://localhost:1337/localhost:8200/turnover_by_day/');
  }
}
