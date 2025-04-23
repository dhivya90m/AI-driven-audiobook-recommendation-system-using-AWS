import boto3
import json
from time import sleep

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

# Load metadata
with open("metadata.json", "r") as f:
    books = json.load(f)

def get_embedding(text):
    payload = {
        "inputText": text,
        "dimensions": 512,
        "normalize": True
    }
    response = bedrock.invoke_model(
        modelId="amazon.titan-embed-text-v2:0",
        contentType="application/json",
        accept="application/json",
        body=json.dumps(payload)
    )
    body = json.loads(response["body"].read().decode("utf-8"))
    return body["embedding"]

updated_books = []
for i, book in enumerate(books):
    try:
        summary = book.get("Summary", "")
        if summary == "No summary available":
            summary = book["Title"] + " " + book["Author"]
        embedding = get_embedding(summary)
        book["Embedding"] = embedding
        print(f"✅ Embedded: {book['FileName']} ({i+1}/{len(books)})")
        updated_books.append(book)
        sleep(0.2)  # slight delay to avoid throttling
    except Exception as e:
        print(f"❌ Failed: {book['FileName']} – {str(e)}")

# Save updated metadata with embeddings
with open("metadata.json", "w") as f:
    json.dump(updated_books, f)

print("\n🎯 Done generating embeddings!")

