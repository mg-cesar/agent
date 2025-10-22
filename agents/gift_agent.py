from models.persona import Persona

class GiftAgent:
    def __init__(self,llm):
        self.llm = llm
    
    def buscar_regalos(self, persona: Persona, presupuesto):
        user_message = (
            f"Quiero regalar un regalo personalizado a una persona de género {persona.genero}, edad {persona.edad}, "
            f"con aficiones: {', '.join(persona.aficiones)}. "
            f"Ya le he regalado antes: {', '.join(persona.historico_regalos)}. "
            f"Mi presupuesto es de {presupuesto} euros. "
            "Qué regalos me recomiendas?"
        )
        messages = [
            ("system", "Eres un asistente útil que busca los mejores regalos personalizados."),
            ("human", user_message)
        ]
        try:
            response = self.llm.invoke(messages)
        except Exception as e:
            print(f"Error al conectar con la API: {e}")
            return None
        return response.content