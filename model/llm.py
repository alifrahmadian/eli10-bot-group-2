from langchain_openai import ChatOpenAI
from config import OPENAI_API_KEY, MODEL_NAME

def get_llm():
    llm = ChatOpenAI(
        model=MODEL_NAME,
        temperature=0.7,
        max_tokens=1000,   
        timeout=30,
        api_key=OPENAI_API_KEY
    )

    return llm