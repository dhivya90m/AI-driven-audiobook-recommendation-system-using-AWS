import boto3
import json

# Initialize DynamoDB resource and specify the table name
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("AudiobookEmbeddings")  # Updated table name

# Load metadata from the generated JSON file
with open("metadata.json", "r") as f:
    metadata_list = json.load(f)

count = 0
for book in metadata_list:
    try:
        # Insert each book metadata into the table
        response = table.put_item(Item=book)
        print(f"✅ Uploaded: {book['FileName']}")
        count += 1
    except Exception as e:
        print(f"❌ Failed: {book['FileName']}, Error: {e}")

print(f"\n🎉 Done! {count} books uploaded to DynamoDB.")

