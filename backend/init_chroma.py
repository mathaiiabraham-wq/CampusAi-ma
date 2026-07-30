import chromadb

# Initialize the client inside the backend/chromadb_data folder
client = chromadb.PersistentClient(path="./chromadb_data")

# Create your collection
collection = client.get_or_create_collection(name="centennial_knowledge_base")

print("Chroma Database initialized in the backend folder!")