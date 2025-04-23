import boto3
import json

s3 = boto3.client("s3")
BUCKET_NAME = "audiobook-data-dhivya"  # ✅ your bucket

def extract_metadata_from_s3_object(key):
    response = s3.get_object(Bucket=BUCKET_NAME, Key=key)
    content = response["Body"].read().decode("utf-8")
    lines = content.strip().split("\n")
    
    title = lines[0] if len(lines) > 0 else "Unknown Title"
    author = lines[1] if len(lines) > 1 else "Unknown Author"
    summary = " ".join(lines[2:]) if len(lines) > 2 else "No summary available"

    return {
        "FileName": key,
        "Title": title.strip(),
        "Author": author.strip(),
        "Summary": summary.strip()
    }

# List all .txt files
paginator = s3.get_paginator("list_objects_v2")
page_iterator = paginator.paginate(Bucket=BUCKET_NAME)

metadata_list = []

for page in page_iterator:
    for obj in page.get("Contents", []):
        key = obj["Key"]
        if key.endswith(".txt"):
            print(f"📖 Processing: {key}")
            metadata = extract_metadata_from_s3_object(key)
            metadata_list.append(metadata)

# Save to metadata.json
with open("metadata.json", "w") as f:
    json.dump(metadata_list, f, indent=2)

print(f"\n✅ Metadata generated for {len(metadata_list)} books in metadata.json")

