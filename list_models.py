import boto3
from botocore.exceptions import ClientError

# Initialize the AWS Bedrock client
bedrock_client = boto3.client('bedrock', region_name='us-west-2')

try:
    # Correct method name
    response = bedrock_client.list_foundation_models()
    
    # Extract model summaries
    models = response.get('modelSummaries', [])
    
    # Print model details
    for model in models:
        print(f"Model Name: {model['modelName']}")
        print(f"Provider: {model['providerName']}")
        print(f"ID: {model['modelId']}\n")
        
except ClientError as e:
    print(f"AWS API Error: {e}")
except KeyError as e:
    print(f"Missing expected response field: {e}")


