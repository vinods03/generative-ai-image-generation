import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { BedrockImageGenerationServiceService } from './bedrock-image-generation-service.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})

export class HomeComponent implements OnInit {

  promptForm: FormGroup = new FormGroup({})
  imageUrl: string = ''

  constructor(
    private formBuilder: FormBuilder,
    private router: Router,
    private activatedRoute: ActivatedRoute,
    private bedrockImageGenerationService: BedrockImageGenerationServiceService
  ) {}

  ngOnInit(): void {

    this.promptForm = this.formBuilder.group(
      {
        prompt: ['', Validators.required]
      }
    )
  }

  onSubmit() {

    if (this.promptForm.valid) {
      let prompt = this.promptForm.value['prompt']
      this.bedrockImageGenerationService.getImageUrl(prompt).subscribe((imageUrl) =>
        this.imageUrl = imageUrl
    )
    }

  }

  onReset() {
    this.promptForm.reset()
    // this.router.navigate([''])
  }

}
