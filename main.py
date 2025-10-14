import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

class Main:
    def __init__(
        self,
        model_name = "gpt-4o",
        temperature = 0,
        max_tokens = 256
    ):
        api_key = os.getenv("OPENAI_API_KEY")
        self.llm = ChatOpenAI(api_key=api_key, model_name=model_name, temperature=temperature, max_tokens=max_tokens)

    def test_connection(self):
        messages = [
            (
                "system",
                "Eres un asistente útil que busca los mejores regalos",
            ),
            ("human", "¿Qué me recomiendas regalar a una persona que le gusta el senderismo?"),

        ]
        response = self.llm.invoke(messages)
        print("Respuesta de Langchain:", response.content)

if __name__ == "__main__":
    main = Main()
    main.test_connection()