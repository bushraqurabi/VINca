
#RAG for info about VIN
import os
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
assert API_KEY, "Set GEMINI_API_KEY in your .env file!"

def build_retriever():
    loader = TextLoader("vin_explainer_rag/data/VIN_doc.txt")
    documents = loader.load()

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    persist_dir = "chroma_db"
    vectordb = Chroma.from_documents(docs, embeddings, persist_directory=persist_dir)

    return vectordb.as_retriever()

def build_qa_chain():
    llm = ChatGoogleGenerativeAI(
         model="models/gemini-1.5-flash-latest",
        temperature=0.5
    )

    retriever = build_retriever()

   
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return qa

def run_vin_info_rag():
    qa_chain = build_qa_chain()
    print("VIN Q&A assistant ready! Type 'exit' to quit.")

    while True:
        query = input("Your question: ").strip()
        if query.lower() == "exit":
            break

        print("\nSearching...\n")
        response = qa_chain.invoke({"query": query})

        print("\nAnswer:\n", response["result"])

        seen_sources = set()
        for doc in response["source_documents"]:
            source = doc.metadata.get("source")
            if source not in seen_sources:
                print("\nSource:", source)
                seen_sources.add(source)


if __name__ == "__main__":
    run_vin_info_rag()
