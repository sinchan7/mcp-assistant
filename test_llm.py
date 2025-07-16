import warnings
warnings.filterwarnings("ignore")

from langchain_community.llms import Ollama

llm = Ollama(model="mistral")

response = llm.invoke("List 3 innovative project ideas using AI.")
print(response)


