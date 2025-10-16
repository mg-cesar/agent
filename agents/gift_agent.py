class GiftAgent:
    def __init__(self,llm):
        self.llm = llm
    
    def buscar_regalos(self):
        messages = [
            ("system", "Eres un asistente útil que busca los mejores regalos."),
            ("human", "¿Qué me recomiendas regalar a una persona que le gusta el senderismo?")
        ]
        try:
            response = self.llm.invoke(messages)
        except Exception as e:
            print(f"Error al conectar con la API: {e}")
            return None
        return response.content