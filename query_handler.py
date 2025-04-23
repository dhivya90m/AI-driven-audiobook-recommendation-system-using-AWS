import boto3
import json
from decimal import Decimal
from boto3.dynamodb.conditions import Key
from math import sqrt

# Replace with your model details
bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('AudiobookEmbeddings')

def generate_query_embedding(text):
    # Sample with Titan — replace with your own as needed
    payload = {
        "inputText": text
    }

    response = bedrock.invoke_model(
        modelId='amazon.titan-embed-text-v1',
        contentType='application/json',
        accept='application/json',
        body=json.dumps(payload)
    )

    response_body = json.loads(response['body'].read())
    return response_body['embedding']

def cosine_similarity(vec1, vec2):
    dot = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = sqrt(sum(a * a for a in vec1))
    norm2 = sqrt(sum(b * b for b in vec2))
    return dot / (norm1 * norm2)

def lambda_handler(event, context):
    query = event.get("query", "Suggest a book about space and time travel.")
    query_embedding = generate_query_embedding(query)

    results = table.scan()
    similarities = []

    for item in results['Items']:
        book_vector = [float(val['N']) for val in item['Embedding']]
        sim = cosine_similarity(query_embedding, book_vector)
        similarities.append((sim, item['FileName']))

    similarities.sort(reverse=True)
    top_books = [book for _, book in similarities[:3]]

    return {
        "statusCode": 200,
        "body": json.dumps({
            "query": query,
            "recommended_books": top_books
        })
    }

