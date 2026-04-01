from chains import chain
from model import llm
from prompts import prompt

def main():
    while True:
        user_input = input("Tanyakan apa saja yang ingin kamu ketahui: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Terima kasih telah menggunakan layanan kami. Sampai jumpa!")
            break
        
        prompt_template = prompt.get_explain_prompt()
        bot_chain = chain.build_chat_chain(prompt_template)
        response = bot_chain.invoke({"topic": user_input})

        print(response.content)


if __name__ == "__main__":
    main()