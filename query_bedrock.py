import boto3
import os

# 🔐 Set the region and model details
region = "us-east-1"
model_id = "anthropic.claude-v2"  # Or try "amazon.titan-text-lite-v1"
bedrock_runtime = boto3.client("bedrock-runtime", region_name=region)
s3 = boto3.client("s3")

bucket = "audiobook-data-dhivya"
prefix = "book_"

# 🧠 Pick one file to test
file_key = f"{prefix}0.txt"
response = s3.get_object(Bucket=bucket, Key=file_key)
text = response["Body"].read().decode("utf-8")

# 🧠 Craft your Gen AI prompt
prompt = f"""Human: Summarize this audiobook briefly and tell me what type of listener would enjoy it.\n\n{text}\n\nAssistant:"""

# 🧠 Send to Claude (or Titan)
response = bedrock_runtime.invoke_model(
    modelId=model_id,
    body=bytes(prompt, "utf-8"),
    contentType="text/plain",
)

result = response["body"].read().decode("utf-8")
print("🧠 Bedrock response:\n")
print(result)
