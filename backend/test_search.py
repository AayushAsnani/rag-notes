from sentence_transformers import SentenceTransformer
from vector_store import search_chunks

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

question = "How does thermal imaging work?"

question_embedding = model.encode(question)

results = search_chunks(
    question_embedding,
    n_results=3
)

print("\nTop Results:\n")

for doc in results["documents"][0]:
    print("=" * 50)
    print(doc[:500])