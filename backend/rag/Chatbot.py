from dotenv import load_dotenv

from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_groq import ChatGroq

from langchain_classic.chains import RetrievalQA


load_dotenv()


# Load embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

# Load Chroma database

db = Chroma(
    persist_directory="rag/chroma_db",
    embedding_function=embeddings
)


# Create retriever

retriever = db.as_retriever(
    search_kwargs={
        "k": 3
    }
)


# Groq LLM

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3
)


# Create RAG chain

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)



def ask_ai(question):

    response = qa_chain.invoke(
        {
            "query": question
        }
    )

    return response["result"]



if __name__ == "__main__":

    while True:

        question = input("\nAsk about Vimal: ")

        if question.lower()=="exit":
            break

        answer = ask_ai(question)

        print("\nAI:", answer)