from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

# Load resume text
loader = TextLoader("data/resume.txt", encoding="utf-8")
documents = loader.load()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print(f"Loaded {len(documents)} document(s)")
print(f"Created {len(chunks)} chunks")

# Gemini embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

# Create ChromaDB
db = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="rag/chroma_db"
)

print("ChromaDB created successfully!")