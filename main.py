from langchain_community.llms import OpenAI

class Main:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        self.llm = OpenAI(openai_api_key=api_key)
    def test_connection(self):
        response = self.llm("Hola, ¿puedes responder?")
        print("Respuesta de Langchain:", response)

if __name__ == "__main__":
    main = Main()
    main.test_connection()