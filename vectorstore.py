# Run this script to create embeddings from the txt files and store it in ChromaDB. Example: poetry run python3 vectorstore.py
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter

load_dotenv()
embeddings = OpenAIEmbeddings()

loader = DirectoryLoader("txt", glob="*.txt", loader_cls=TextLoader, show_progress=True)
documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

db = Chroma.from_documents(docs, embeddings, persist_directory="vectorstore")

query = "Kan ik parkeren?"
docs = db.similarity_search(query)
print(docs)