from pdf_utils import extract_text_from_pdf
from chunker import chunk_text

pdf_path = "uploads/AI-Assisted_Non-Invasive_Turtle_Nest_Detection_and_Safe_Relocation_System.pdf"

text = extract_text_from_pdf(pdf_path)

chunks = chunk_text(text)

print("Number of chunks:", len(chunks))

print("\nFirst Chunk:\n")
print(chunks[0])