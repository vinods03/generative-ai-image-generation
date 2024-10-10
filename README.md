The idea of this project is to generate a poster / image using the Prompt provided to the model.
This is a completely serverless architecture where the Prompt is passed to Bedrock from a static website (developed in Angular and hosted in S3) through API gateway and Lambda. The image generation is done by the stability.stable-diffusion-xl-v1 model from Stability AI.
The generated image is uploaded into an S3 bucket and a pre-signed URL is returned to the user to access the image.
Please note that the frontend is a very basic structure. The focus of this project is more towards using Amazon Bedrock and integrating multiple AWS services with Bedrock.
