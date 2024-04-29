#1)
import os


class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, number):
        if self._successor:
            return self._successor.handle_request(number)
        return False  


class PrimoHandler(Handler):
    def handle_request(self, number):
        if self._is_primo(number):
            print(f"PrimoHandler: Consumido {number}")
            return True
        else:
            return super().handle_request(number)

    def _is_primo(self, number):
        if number <= 1:
            return False
        if number <= 3:
            return True
        if number % 2 == 0 or number % 3 == 0:
            return False
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        return True


class ParHandler(Handler):
    def handle_request(self, number):
        if number % 2 == 0:
            print(f"ParHandler: Consumido {number}")
            return True
        else:
            return super().handle_request(number)


class NoConsumidoHandler(Handler):
    def handle_request(self, number):
        print(f"NoConsumidoHandler: {number} no fue consumido")


class CadenaResponsabilidad:
    def __init__(self):
        self._handler_chain = PrimoHandler(ParHandler(NoConsumidoHandler()))

    def procesar_numeros(self):
        for number in range(1, 101):
            self._handler_chain.handle_request(number)


cadena_responsabilidad = CadenaResponsabilidad()
cadena_responsabilidad.procesar_numeros()

#2)
class IteradorCadena:
    def __init__(self, cadena):
        self._cadena = cadena
        self._indice = 0
        self._sentido = 1

    def __iter__(self):
        return self

    def __next__(self):
        if 0 <= self._indice < len(self._cadena):
            char = self._cadena[self._indice]
            self._indice += self._sentido
            return char
        else:
            raise StopIteration

    def reverso(self):
        self._indice = len(self._cadena) - 1
        self._sentido = -1

cadena = "Hola Mundo"
iterador = IteradorCadena(cadena)

print("Recorrido directo:")
for char in iterador:
    print(char)

iterador.reverso()
print("\nRecorrido reverso:")
for char in iterador:
    print(char)
    
#3)
class Sujeto:
    def __init__(self):
        self._observadores = []

    def suscribir(self, observador):
        self._observadores.append(observador)

    def notificar(self, id_emisor):
        for observador in self._observadores:
            observador.actualizar(id_emisor)


class Observador:
    def __init__(self, id_propio):
        self._id_propio = id_propio

    def actualizar(self, id_emisor):
        if id_emisor == self._id_propio:
            print(f"¡Mensaje recibido por Observador {self._id_propio}: Coincide el ID!")


observador1 = Observador("ABCD")
observador2 = Observador("EFGH")
observador3 = Observador("WXYZ")
observador4 = Observador("1234")

sujeto = Sujeto()
sujeto.suscribir(observador1)
sujeto.suscribir(observador2)
sujeto.suscribir(observador3)
sujeto.suscribir(observador4)

print("\nEmisión de IDs:")
for i in range(8):
    id_emisor = input("Ingrese un ID de 4 caracteres: ")
    sujeto.notificar(id_emisor)

#4)
class State:
    def __init__(self):
        self.memorized_am_stations = ["M1: 1250", "M2: 1380", "M3: 1510"]  # Frecuencias memorizadas de AM
        self.memorized_fm_stations = ["M4: 95.5", "M5: 98.7", "M6: 101.1"]  # Frecuencias memorizadas de FM

    def scan(self):
        print("Escaneando estaciones AM:")
        for station in self.stations:
            print(f"Sintonizando... Estación {station}")

        print("\nEscaneando estaciones FM:")
        for station in self.fm_stations:
            print(f"Sintonizando... Estación {station}")

        print("\nSintonizando frecuencias memorizadas de AM:")
        for station in self.memorized_am_stations:
            print(station)

        print("\nSintonizando frecuencias memorizadas de FM:")
        for station in self.memorized_fm_stations:
            print(station)


class AmState(State):
    def __init__(self, radio):
        super().__init__()
        self.stations = ["1250", "1380", "1510"]
        self.radio = radio

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate


class FmState(State):
    def __init__(self, radio):
        super().__init__()
        self.stations = ["95.5", "98.7", "101.1"]
        self.radio = radio
        

#5)
class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content


class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""
        self.past_states = []

    def write(self, string):
        self.content += string

    def save(self):
        if len(self.past_states) == 4:
            self.past_states.pop(0)  
        self.past_states.append(Memento(self.file, self.content))

    def undo(self, steps):
        if steps > len(self.past_states):
            print("No hay suficientes estados en el pasado para deshacer")
            return
        memento = self.past_states[-steps]
        self.file = memento.file
        self.content = memento.content

    def get_current_state(self):
        return self.content


class FileWriterCaretaker:
    def save(self, writer):
        writer.save()

    def undo(self, writer, steps):
        writer.undo(steps)


if __name__ == '__main__':
    os.system("clear")
    print("Crea un objeto que gestionará la versión anterior")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    print("Se graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.get_current_state() + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.get_current_state() + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional II")
    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.get_current_state() + "\n\n")

    print("Se invoca al <undo> para deshacer un paso")
    caretaker.undo(writer, 1)
    print("Se muestra el estado actual:")
    print(writer.get_current_state() + "\n\n")

    print("Se invoca al <undo> para deshacer dos pasos")
    caretaker.undo(writer, 2)
    print("Se muestra el estado actual:")
    print(writer.get_current_state() + "\n\n")