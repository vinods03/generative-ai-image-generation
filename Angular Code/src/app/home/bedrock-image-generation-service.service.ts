import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class BedrockImageGenerationServiceService {

  private apiGetImageUrl = 'https://4dcyq1di1g.execute-api.us-east-1.amazonaws.com/prod/bedrock-image-generation-resource'
  constructor(private http: HttpClient) {}

  getImageUrl(prompt: string): Observable<string> {
    return this.http.get<string>(this.apiGetImageUrl+'?prompt='+prompt)
  }
}
