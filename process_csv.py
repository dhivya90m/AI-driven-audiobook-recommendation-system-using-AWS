import pandas as pd
import os

# Load CSV file - change filename if different
csv_path = "/home/cloudshell-user/audiobooks.csv"
df = pd.read_csv(csv_path)

# Helper function to clean text
def clean(text):
    if pd.isnull(text):
        return ""
    return text.replace('\n', ' ').strip()

# Combine title, author, and description
df['combined'] = df.apply(
    lambda row: f"Title: {clean(row.get('title'))}\nAuthor: {clean(row.get('author'))}\n\n{clean(row.get('description'))}",
    axis=1
)

# Create a folder for chunks
os.makedirs("chunks", exist_ok=True)

# Save each combined row to a text file
for i, text in enumerate(df['combined'].dropna()):
    with open(f"chunks/book_{i}.txt", "w", encoding="utf-8") as f:
        f.write(text)

print(f"✅ {len(df)} audiobook entries processed into chunks!")

