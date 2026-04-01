from services.rag_service import ask_question

question = "What is the leave policy?"

answer = ask_question(question)

print("\nAnswer:\n", answer)