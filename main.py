from langchain_community.llms import OpenAI

class Main:
    def __init__(self):
        self.llm = OpenAI(openai_api_key="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")
    def test_connection(self):
        response = self.llm("Hola, ¿puedes responder?")
        print("Respuesta de Langchain:", response)

if __name__ == "__main__":
    main = Main()
    main.test_connection()