import json
import boto3
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('AudiobookEmbeddings')

# Load metadata with embeddings
with open('metadata.json', 'r') as f:
    metadata = json.load(f)

count = 0

for book in metadata:
    if 'Embedding' not in book or not book['Embedding']:
        print(f"⛔ Skipping: {book.get('FileName', 'unknown')} (no embedding)")
        continue

    embedding_decimal = [Decimal(str(x)) for x in book['Embedding']]

    try:
        table.update_item(
            Key={'FileName': book['FileName']},
            UpdateExpression='SET #E = :e',
            ExpressionAttributeNames={'#E': 'Embedding'},
            ExpressionAttributeValues={':e': embedding_decimal}
        )
        print(f"✅ Embedded: {book['FileName']}")
        count += 1
    except Exception as e:
        print(f"❌ Failed: {book['FileName']} – {e}")

print(f"\n✨ Updated {count} items with embeddings.")

