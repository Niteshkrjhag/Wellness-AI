# when we want to add new book as data for our system we need to again make embedding of all the 
# data we have even we had already made embeddings and stored in vector db.
# so we created this file so that only new data get converted to embedding and stored in the 
# vector db.
from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore

from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY


extracted_data = load_pdf_file(data = 'data/')
text_chunks = text_split(extracted_data)
embeddings_model = download_hugging_face_embeddings()


pc = Pinecone(api_key= PINECONE_API_KEY)

index_name = "wellnessai"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        vector_type="dense",
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        ),
        deletion_protection="disabled",
        tags={
            "environment": "development"
        }
    )


# Embed each chunk and upsert the embeddings into our Pinecone index.
docsearch = PineconeVectorStore.from_documents(
    documents = text_chunks,
    index_name = index_name,
    embedding = embeddings_model
)