import json
import boto3
import base64
import datetime

client_bedrock = boto3.client('bedrock-runtime')
client_s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    # capture the input prompt
    print(boto3.__version__)
    print('The event is: ', event)
    prompt = event['prompt']
    print('The prompt is: ', prompt)
    
    # invoke the image generation model using the above prompt
    # text – The prompt that you want to pass to the model.
    # weight (Optional) – The weight that the model should apply to the prompt. A value that is less than zero declares a negative prompt.  Use a negative prompt to tell the model to avoid certain concepts. The default value for weight is one.
    # cfg_scale (Optional) - Determines how much the final image portrays the prompt. Use a lower number to increase randomness in the generation. Minimum: 0, Maximum: 35, Default: 7
    # steps – (Optional) Generation step determines how many times the image is sampled. More steps can result in a more accurate result. Minimum: 10, Maximum: 150, Default: 30
    # samples – (Optional) The number of image to generate. Currently Amazon Bedrock supports generating one image. If you supply a value for samples, the value must be one.
    # height – (Optional) Height of the image to generate, in pixels, in an increment divisible by 64. The value must be one of 1024x1024, 1152x896, 1216x832, 1344x768, 1536x640, 640x1536, 768x1344, 832x1216, 896x1152.
    # width – (Optional) Width of the image to generate, in pixels, in an increment divisible by 64. The value must be one of 1024x1024, 1152x896, 1216x832, 1344x768, 1536x640, 640x1536, 768x1344, 832x1216, 896x1152.    response_bedrock = client_bedrock.invoke_model(
    # seed – (Optional) The seed determines the initial noise setting. Use the same seed and the same settings as a previous run to allow inference to create a similar image. If you don't set this value, or the value is 0, it is set as a random number.
             # Minimum: 0, Default: 0, Maximum: 4294967295
    response_bedrock = client_bedrock.invoke_model(
        contentType='application/json', 
        accept='application/json', 
        modelId='stability.stable-diffusion-xl-v1',
        body=json.dumps({'text_prompts':[{'text':prompt,'weight':1}],'cfg_scale':35,'steps':100,'seed':0,'width':1024,'height':1024,'samples':1})
    )
    print('The response from bedrock is: ', response_bedrock)
    
    # convert the response from bedrock which is a streaming body, into bytes
    response_bedrock_byte = json.loads(response_bedrock['body'].read())
    print('response_bedrock_byte is: ', response_bedrock_byte)
    
    # encode the bytes into actual image
    response_bedrock_base64 = response_bedrock_byte['artifacts'][0]['base64']
    response_bedrock_finalimage = base64.b64decode(response_bedrock_base64)
    print(response_bedrock_finalimage)
    
    # upload the image into S3 bucket
    s3_image_file = 'image-'+datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    response_s3 = client_s3.put_object(
        Bucket='vinodmovieposterdesign',
        Key=s3_image_file,
        Body=response_bedrock_finalimage
        )
        
    # create a pre-signed url and return it
    presigned_url = client_s3.generate_presigned_url('get_object', Params={'Bucket':'vinodmovieposterdesign','Key':s3_image_file}, ExpiresIn=600)
    return {
        'statusCode': 200,
        'body': presigned_url
    }

