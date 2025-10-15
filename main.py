import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

class Main:
    def __init__(
        self,
        model_name: str = "gpt-4o",
        temperature: float = 0,
        max_tokens: int = 256
    ):
        """
        Inicializa el cliente de ChatOpenAI.
        
        Args:
            model_name: Nombre del modelo a utilizar
            temperature: Temperatura para la generación (0-1)
            max_tokens: Número máximo de tokens en la respuesta
        """
        api_key = os.getenv("OPENAI_API_KEY")
        
        # Validar que la API key existe
        if not api_key:
            raise ValueError("OPENAI_API_KEY no encontrada en las variables de entorno")
        
        self.llm = ChatOpenAI(
            api_key=api_key,
            model_name=model_name,
            temperature=temperature,
            max_tokens=max_tokens
        )

    def test_connection(self):
        """
        Prueba la conexión con la API de OpenAI.
        """
        messages = [
            (
                "system",
                "Eres un asistente útil que busca los mejores regalos",
            ),
            (
                "human",
                "¿Qué me recomiendas regalar a una persona que le gusta el senderismo?"
            ),
        ]
        
        try:
            response = self.llm.invoke(messages)
            print("Respuesta de Langchain:", response.content)
        except Exception as e:
            print(f"Error al conectar con la API: {e}")

if __name__ == "__main__":
    try:
        main = Main()
        main.test_connection()
    except ValueError as e:
        print(f"Error de configuración: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")