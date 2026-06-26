from pdf_utils import extract_text_from_pdf
from chunker import chunk_text
from embeddings import generate_embeddings

pdf_path = "uploads/AI-Assisted_Non-Invasive_Turtle_Nest_Detection_and_Safe_Relocation_System.pdf"

text = extract_text_from_pdf(pdf_path)

chunks = chunk_text(text)

embeddings = generate_embeddings(chunks)

print("Chunks:", len(chunks))
print("Embeddings:", len(embeddings))
print("Embedding Dimension:", len(embeddings[0]))