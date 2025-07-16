from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="mistral")

response = llm.invoke("Give me 3 startup ideas using AI.")
print(response)
