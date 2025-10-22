class GiftAgent:
    def __init__(self,llm):
        self.llm = llm
    
    def buscar_regalos(self, aficiones, genero, edad, historico_regalos, presupuesto):
        user_message = (
            f"Quiero regalar un regalo personalizado a una persona de género {genero}, edad {edad}, "
            f"con aficionaes: {', '.join(aficiones)}. "
            f"Ya le he regalado antes: {', '.join(historico_regalos)}. "
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