from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Initialize the model
llm = Ollama(model="mistral")

# Prompt template for summarization
template = """
You are a helpful assistant. Summarize the following text clearly and concisely:

{text}
"""

prompt = PromptTemplate.from_template(template)
chain = LLMChain(llm=llm, prompt=prompt)

def summarize(command):
    # Extract the text after the keyword
    text = command.replace("summarize", "").strip()
    
    if not text:
        return "❌ MCP: Please provide the text you want me to summarize."
    
    try:
        summary = chain.run(text)
        return f"📝 MCP Summary:\n{summary}"
    except Exception as e:
        return f"❌ MCP: Failed to summarize. {e}"
