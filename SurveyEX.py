class Estudiante:
    def __init__(self, nombre, edad, proyecto, equipo, libreria):
        self.nombre = nombre
        self.edad = edad
        self.proyecto = proyecto
        self.equipo = equipo
        self.libreria = libreria

    def __str__(self):
        return f"{self.nombre} ({self.edad} años) → Proyecto: {self.proyecto}, Equipo: {self.equipo}, Librería: {self.libreria}"

class Encuesta:
    def __init__(self, preguntas):
        self.preguntas = preguntas
        self.respuestas = []

    def agregar_respuesta(self, estudiante):
        self.respuestas.append(estudiante)

    def mostrar_resultados(self):
        print("\n Resultados de la Encuesta:")
        for est in self.respuestas:
            print(est)

    def resumen(self):
        conteo = {}
        for est in self.respuestas:
            conteo[est.proyecto] = conteo.get(est.proyecto, 0) + 1

        print("\n Resumen de ideas de proyectos:")
        for proyecto, votos in conteo.items():
            print(f"- {proyecto}: {votos} votos")

preguntas = [
    "¿Qué tema prefieres para el proyecto?",
    "¿Sabes trabajar en equipo? (sí/no)",
    "¿Conoces alguna librería de Python?"
]

encuesta = Encuesta(preguntas)

print("===== Encuesta de Ideas de Proyecto =====")

for i in range(3): 
    print(f"\n Estudiante {i+1}")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    proyecto = input(preguntas[0] + " ")
    equipo = input(preguntas[1] + " ")
    libreria = input(preguntas[2] + " ")

    estudiante = Estudiante(nombre, edad, proyecto, equipo, libreria)
    encuesta.agregar_respuesta(estudiante)

encuesta.mostrar_resultados()
encuesta.resumen()
