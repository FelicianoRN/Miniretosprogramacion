import random

class JJOO:
    def __init__(self):
        self.eventos = {}
        self.participantes = {}
        self.resultados = {}

    def registrar_evento(self, evento):
        if evento not in self.eventos:
            self.eventos[evento] = []
            print(f"Evento '{evento}' registrado.")
        else:
            print(f"El evento '{evento}' ya está registrado.")

    def registrar_participante(self, nombre, pais):
        if nombre not in self.participantes:
            self.participantes[nombre] = pais
            print(f"Participante '{nombre}' de '{pais}' registrado.")
        else:
            print(f"El participante '{nombre}' ya está registrado.")

    def asignar_participante_evento(self, evento, participante):
        if evento in self.eventos and participante in self.participantes:
            self.eventos[evento].append(participante)
            print(f"Participante '{participante}' asignado al evento '{evento}'.")
        else:
            print("Evento o participante no registrado.")

    def simular_evento(self, evento):
        if evento in self.eventos and len(self.eventos[evento]) >= 3:
            participantes = self.eventos[evento]
            random.shuffle(participantes)
            self.resultados[evento] = {
                "oro": participantes[0],
                "plata": participantes[1],
                "bronce": participantes[2]
            }
            print(f"Evento '{evento}' simulado.")
        else:
            print("Evento no registrado o no tiene suficientes participantes.")

    def mostrar_ganadores(self, evento):
        if evento in self.resultados:
            print(f"Ganadores del evento '{evento}':")
            print(f"Oro: {self.resultados[evento]['oro']}")
            print(f"Plata: {self.resultados[evento]['plata']}")
            print(f"Bronce: {self.resultados[evento]['bronce']}")
        else:
            print(f"No hay resultados para el evento '{evento}'.")

    def ranking_paises(self):
        medallero = {}
        for resultado in self.resultados.values():
            for medalla, participante in resultado.items():
                pais = self.participantes[participante]
                if pais not in medallero:
                    medallero[pais] = {"oro": 0, "plata": 0, "bronce": 0}
                medallero[pais][medalla] += 1

        ranking = sorted(medallero.items(), key=lambda x: (x[1]['oro'], x[1]['plata'], x[1]['bronce']), reverse=True)
        print("Ranking de países:")
        for pais, medallas in ranking:
            print(f"{pais}: Oro: {medallas['oro']}, Plata: {medallas['plata']}, Bronce: {medallas['bronce']}")

    def menu(self):
        while True:
            print("\nMenú:")
            print("1. Registro de eventos")
            print("2. Registro de participantes")
            print("3. Asignar participante a evento")
            print("4. Simulación de eventos")
            print("5. Mostrar ganadores")
            print("6. Ranking de países")
            print("7. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                evento = input("Ingrese el nombre del evento: ")
                self.registrar_evento(evento)
            elif opcion == "2":
                nombre = input("Ingrese el nombre del participante: ")
                pais = input("Ingrese el país del participante: ")
                self.registrar_participante(nombre, pais)
            elif opcion == "3":
                evento = input("Ingrese el nombre del evento: ")
                participante = input("Ingrese el nombre del participante: ")
                self.asignar_participante_evento(evento, participante)
            elif opcion == "4":
                evento = input("Ingrese el nombre del evento: ")
                self.simular_evento(evento)
            elif opcion == "5":
                evento = input("Ingrese el nombre del evento: ")
                self.mostrar_ganadores(evento)
            elif opcion == "6":
                self.ranking_paises()
            elif opcion == "7":
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida.")

if __name__ == "__main__":
    jjoo = JJOO()
    jjoo.menu()