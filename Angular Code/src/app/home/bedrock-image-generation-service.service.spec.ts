import { TestBed } from '@angular/core/testing';

import { BedrockImageGenerationServiceService } from './bedrock-image-generation-service.service';

describe('BedrockImageGenerationServiceService', () => {
  let service: BedrockImageGenerationServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(BedrockImageGenerationServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
