from model.llm import get_llm

llm = get_llm()

def build_chat_chain(prompt):
    return prompt | llm
