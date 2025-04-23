# 🎧 AI-Driven Audiobook Recommendation System Using AWS

This project is an **AI-driven audiobook recommendation system** that leverages the power of **Amazon Bedrock** for embeddings, **AWS Lambda** for serverless computation, **DynamoDB** for data storage, and **S3** for metadata. It processes raw audiobook data, generates meaningful embeddings, and provides personalized audiobook recommendations based on user queries.

The system is designed to recommend audiobooks based on the user's natural language query, making it intuitive and efficient for users to discover content aligned with their interests.

---

## 🎯 Goal

The objective of this project is to provide a **personalized audiobook recommendation engine** using **semantic search** powered by **AI embeddings**. Users can input natural language queries like:

- "Find me a book about mindfulness."
- "Suggest something related to habits and success."
  
The system will process these queries and recommend relevant audiobooks from a dataset, ensuring a seamless and user-friendly experience.

---

## 🧠 Key Features

- ✅ **Semantic Search**: Convert user queries into embeddings and match them with the audiobook dataset.
- ✅ **Serverless Architecture**: Using AWS Lambda to handle incoming queries efficiently.
- ✅ **Scalable**: Process large datasets and store embeddings in DynamoDB for fast lookups.
- ✅ **AI-Powered Recommendations**: Use **Amazon Titan Embeddings** (via **Bedrock**) to generate embeddings and perform similarity comparisons.
- ✅ **Chunking for Efficiency**: Data is chunked into 512-character segments for optimized processing and memory management.
- ✅ **Fully Automated Pipeline**: From data processing to deployment, everything is automated using Python scripts.

---

## 📊 Tech Stack

| Component            | Tech Used                           |
|----------------------|--------------------------------------|
| **Embedding Model**   | Amazon Titan (via Bedrock)           |
| **Data Processing**   | Python, Pandas, Boto3                |
| **Data Storage**      | DynamoDB, S3                        |
| **Serverless API**    | AWS Lambda + API Gateway            |
| **CI/CD & Deployment**| AWS CloudShell, Lambda, API Gateway |
| **Authentication**    | IAM Policies                        |
| **Query Execution**   | Python Scripts for Query Handling   |

---

## 🧩 Project Workflow

1. **Data Processing**  
   - The raw audiobook data is stored in `audiobooks.csv`.
   - The CSV file is chunked into smaller segments (512 characters each) to make it suitable for embedding processing.
   - The chunks are processed and saved into S3 for further embedding generation.

2. **Metadata Extraction**  
   - Metadata (e.g., book title, author) is extracted and stored in `metadata.json`.
   - This metadata is then pushed to DynamoDB for fast lookups during the recommendation process.

3. **Embedding Generation**  
   - **Amazon Titan** embeddings are generated for each chunked text using **Amazon Bedrock**.
   - These embeddings capture the semantic meaning of the text, allowing for accurate content matching based on similarity.

4. **Store Embeddings**  
   - The generated embeddings are stored in **DynamoDB** for easy retrieval when a user query is processed.
   - Metadata is also stored in DynamoDB to provide context (e.g., title, author) for the recommendations.

5. **Serverless API**  
   - **AWS Lambda** handles incoming queries, generates embeddings for the query, and compares it with the stored embeddings.
   - **API Gateway** is used to expose the Lambda function as a RESTful API for easy access.
   - **Cosine similarity** is used to compare query embeddings with book embeddings, and the top matches are returned to the user.

6. **Recommendation Response**  
   - The API responds with a list of recommended audiobooks based on the user’s query and the similarity scores of the embeddings.

---

## 🛠️ Project Structure

```bash
audiobook-genai/
├── audiobooks.csv                     # Raw audiobook dataset (CSV format)
├── chunks/                            # Folder for chunked text files (from the CSV)
├── metadata.json                      # S3-based metadata of the audiobooks
├── output.txt                         # Sample output logs for reference
│
├── process_csv.py                     # Script to chunk the CSV data into smaller segments
├── generate_embeddings.py            # Script to generate embeddings using Amazon Titan (via Bedrock)
├── update_embeddings.py              # Script to store embeddings in DynamoDB
├── generate_metadata_from_s3.py      # Extract metadata from S3 and prepare it for storage
├── update_dynamodb_metadata.py       # Push extracted metadata to DynamoDB
├── update_dynamodb_from_json.py      # Optional script to update metadata in DynamoDB in batch
│
├── query_handler.py                  # AWS Lambda function to handle incoming queries and return recommendations
├── query_bedrock.py                  # Local script to test queries with Amazon Bedrock embeddings
├── list_models.py                    # Helper script to list all available Bedrock models
├── details_model.py                  # Helper script to fetch details about Titan embedding models
│
├── titan_policy.json                 # IAM policy for accessing Amazon Bedrock services securely
├── requirements.txt                  # List of required Python packages (e.g., boto3, pandas)
└── README.md                         # Project documentation

## 🧑‍💻 Detailed Explanation of Key Python Scripts

This section provides an in-depth explanation of the key Python scripts used in this project. Each script serves a specific purpose in processing data, generating embeddings, and handling queries. Below is a breakdown of each script:

### 1. `process_csv.py`

This script processes the raw `audiobooks.csv` file by splitting it into smaller text chunks (512 characters per chunk). This chunking makes it easier to process large volumes of text and ensures memory efficiency when generating embeddings.

### 2. `generate_embeddings.py`

This script interacts with **Amazon Bedrock** to generate embeddings for each text chunk. It sends a batch of text chunks to **Titan** (the embedding model), which then returns a vector representation for each chunk. These vectors are stored in a format suitable for querying later.

### 3. `update_embeddings.py`

Once the embeddings are generated, this script stores them in **DynamoDB**, along with metadata such as book titles and authors. The embeddings are stored as numerical arrays for future retrieval during the query process.

### 4. `generate_metadata_from_s3.py`

This script pulls metadata from **S3**, such as book titles and authors, and formats it for storage in **DynamoDB**. Metadata is essential for providing context to the recommendations.

### 5. `query_handler.py`

This is the core of the **AWS Lambda function**. It receives the user query via **API Gateway**, generates an embedding for the query, and compares it with the stored embeddings in **DynamoDB** using cosine similarity. The Lambda function returns the top 3 most relevant audiobooks to the user.

### 6. `query_bedrock.py`

A local testing script to simulate queries and see how well the Bedrock embedding model responds. This script is used for testing purposes before deploying the Lambda function.

### 7. `list_models.py`

A utility script that lists all available models in **Amazon Bedrock**. It helps you identify and interact with the models you plan to use in your workflow.

### 8. `details_model.py`

This script fetches detailed information about the **Titan model** used for embedding generation. It allows you to examine model parameters and settings.

## 📝 Prerequisites

Before running the scripts, make sure you have the following set up:

- **AWS account** with permissions to use Bedrock, DynamoDB, Lambda, and API Gateway.
- **AWS CLI** configured with the necessary credentials.
- **Python 3.7+** and the required libraries installed. You can install the libraries by running:
