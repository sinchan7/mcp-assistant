from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Initialize model
llm = Ollama(model="mistral")

# Prompt template
template = """
Act like a creative strategist. Brainstorm 5 unique, useful, and innovative ideas for the following topic:

Topic: {topic}

Give the ideas as a numbered list.
"""

prompt = PromptTemplate.from_template(template)
chain = LLMChain(llm=llm, prompt=prompt)

def generate_ideas(command):
    topic = command.replace("brainstorm", "").strip()
    if not topic:
        return "❌ MCP: Please provide a topic to brainstorm."
    
    try:
        ideas = chain.run(topic)
        return f"💡 MCP Ideas:\n{ideas}"
    except Exception as e:
        return f"❌ MCP: Failed to brainstorm ideas. {e}"

