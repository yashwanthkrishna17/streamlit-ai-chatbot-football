from langchain_ollama import ChatOllama
from langchain_ollama import ChatOllama
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="phi3:mini"
)
def ask(context, query):

    prompt = f"""
You are a football scout.

Context:

{context}

Question:

{query}

Answer only using context.
"""

    res = llm.invoke(
        prompt
    )

    return res.content