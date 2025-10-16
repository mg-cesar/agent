import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from agents.gift_agent import GiftAgent
from agents.travel_agent import TravelAgent

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

if __name__ == "__main__":
    try:
        main = Main()
        print("Elige el agente:")
        print("1. Buscar regalos")
        print("2. Buscar actividades en un viaje")
        opcion = input("Introduce 1 o 2: ")
        if opcion == "1":
            agente = GiftAgent(main.llm)
            print(agente.buscar_regalos())
        elif opcion == "2":
            agente = TravelAgent(main.llm)
            print(agente.buscar_actividades())
        else:
            print("Opción no válida.")
    except ValueError as e:
        print(f"Error de configuración: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")