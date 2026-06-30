from fastapi import FastAPI, UploadFile, File
from chunker import chunk_text
from embeddings import generate_embeddings
from vector_store import store_chunks
import os

from pdf_utils import extract_text_from_pdf

app = FastAPI()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {"message": "RAG Notes AI Backend Running"}


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Step 1: Extract text
    extracted_text = extract_text_from_pdf(file_path)

    # Step 2: Split into chunks
    chunks = chunk_text(extracted_text)

    # Step 3: Generate embeddings
    embeddings = generate_embeddings(chunks)

    # Step 4: Store everything in ChromaDB
    store_chunks(chunks, embeddings)

    # Step 5: Return success
    return {
        "message": "PDF uploaded and indexed successfully!",
        "filename": file.filename,
        "chunks": len(chunks)
    }