import os

from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_community.vectorstores import Chroma


load_dotenv()


# Location of resume data
DATA_PATH = "data/resume.txt"


# Load resume text

loader = TextLoader(
    DATA_PATH,
    encoding="utf-8"
)

documents = loader.load()


print("Loaded documents:", len(documents))



# Split text into chunks

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)


chunks = text_splitter.split_documents(documents)


print("Created chunks:", len(chunks))



# Create embeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)



# Store in ChromaDB

db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)


db.persist()


print("ChromaDB created successfully!")