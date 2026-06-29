from embeddings import model
from vector_store import search_chunks
from gemini_client import generate_answer


def ask_question(question):

    # Step 1
    question_embedding = model.encode(question)

    # Step 2
    results = search_chunks(question_embedding)

    # Step 3
    retrieved_chunks = results["documents"][0]

    context = "\n\n".join(retrieved_chunks)

    # Step 4
    answer = generate_answer(context, question)

    return answer