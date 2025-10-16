class TravelAgent:
    def __init__(self, llm):
        self.llm = llm

    def buscar_actividades(self):
        messages = [
            ("system", "Eres un asistente experto en viajes y actividades turísticas."),
            ("human", "¿Qué actividades puedo hacer en un viaje a Barcelona?")
        ]
        try:
            response = self.llm.invoke(messages)
        except Exception as e:
            print(f"Error al conectar con la API: {e}")
            return None
        return response.content