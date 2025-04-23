import boto3
import json

# Load metadata
with open("metadata.json", "r") as f:
    book_metadata = json.load(f)

# Connect to DynamoDB
dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
table = dynamodb.Table("AudiobookEmbeddings")

# Update items
for book in book_metadata:
    try:
        response = table.update_item(
            Key={"FileName": book["FileName"]},
            UpdateExpression="SET #title = :title, #author = :author, #summary = :summary",
            ExpressionAttributeNames={
                "#title": "Title",
                "#author": "Author",
                "#summary": "Summary"
            },
            ExpressionAttributeValues={
                ":title": book["Title"],
                ":author": book["Author"],
                ":summary": book["Summary"]
            }
        )
        print(f"✅ Updated {book['FileName']}")
    except Exception as e:
        print(f"❌ Error updating {book['FileName']}: {str(e)}")

