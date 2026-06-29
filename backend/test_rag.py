from rag import ask_question

question = input("Ask a question: ")

answer = ask_question(question)

print("\nAnswer:\n")
print(answer)