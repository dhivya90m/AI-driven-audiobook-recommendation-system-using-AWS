# Filter by provider and modality
response = bedrock_client.list_foundation_models(
    byProvider='anthropic',
    byOutputModality='TEXT'
)

