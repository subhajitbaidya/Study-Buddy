from youtube_transcript_api import YouTubeTranscriptApi
from langchain_ollama import OllamaEmbeddings
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

embeddings = OllamaEmbeddings(model="llama3.2:latest")


def create_vector_db(video_url: str) -> FAISS:
    # Extract video ID from URL
    video_id = video_url.split("v=")[-1].split("&")[0]

    # Fetch transcript
    transcript_list = YouTubeTranscriptApi.get_transcript(
        video_id, languages=['en'])
    full_text = " ".join([t["text"] for t in transcript_list])

    # Wrap transcript in LangChain Document
    docs = [Document(page_content=full_text, metadata={"source": video_url})]

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=50)
    split_docs = text_splitter.split_documents(docs)

    # Build FAISS vector store
    db = FAISS.from_documents(split_docs, embeddings)
    return db


if __name__ == "__main__":
    db = create_vector_db("https://www.youtube.com/watch?v=QsYGlZkevEg")

    # Test search
    results = db.similarity_search("What is the video about?", k=3)
    for r in results:
        print(r.page_content, "\n---")
