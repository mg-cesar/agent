class Persona:
    def __init__(self, edad, genero, aficiones, historico_regalos):
        self.edad = edad
        self.genero =genero
        self.aficiones = aficiones
        self.historico_regalos = historico_regalos
    
    def __str__(self):
        return(
            f"Persona(edad={self.edad}, genero={self.genero}, "
            f"aficiones={self.aficiones}, historico_regalos={self.historico_regalos}, "
            )
        