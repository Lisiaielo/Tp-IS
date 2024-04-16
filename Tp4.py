
# 1. Provea una clase ping que luego de creada al ser invocada con un método 
# “execute(string)” realice 10 intentos de ping a la dirección IP contenida en 
# “string” (argumento pasado), la clase solo debe funcionar si la dirección IP 
# provista comienza con “192.”. Provea un método executefree(string) que haga 
# lo mismo pero sin el control de dirección. Ahora provea una clase pingproxy 
# cuyo método execute(string) si la dirección es “192.168.0.254” realice un ping a 
# www.google.com usando el método executefree de ping y re-envie a execute 
# de la clase ping en cualquier otro caso. (Modele la solución como un patrón 
# proxy).
class Ping:
    def execute(self, ip_address):
        if ip_address.startswith("192."):
            for _ in range(10):
                response = os.system("ping -c 1 " + ip_address)

class PingProxy:
    def __init__(self):
        self.ping = Ping()

    def execute(self, ip_address):
        if ip_address == "192.168.0.254":
            self.ping.executefree("www.google.com")
        else:
            self.ping.execute(ip_address)

    def executefree(self, ip_address):
        self.ping.executefree(ip_address)

# 2. Para un producto láminas de acero de 0.5” de espesor y 1,5 metros de ancho 
# dispone de dos trenes laminadores, uno que genera planchas de 5 mts y otro 
# de 10 mts. Genere una clase que represente a las láminas en forma genérica al 
# cual se le pueda indicar que a que tren laminador se enviará a producir. (Use el 
# patrón bridge en la solución).
class Lamina:
    def __init__(self, ancho, tren_laminador):
        self.ancho = ancho
        self.tren_laminador = tren_laminador

    def producir(self):
        return self.tren_laminador.producir_lamina(self.ancho)

class TrenLaminador:
    def producir_lamina(self, ancho):
        pass

class TrenLaminador5(TrenLaminador):
    def producir_lamina(self, ancho):
        pass

class TrenLaminador10(TrenLaminador):
    def producir_lamina(self, ancho):
        pass

# 3. Represente la lista de piezas componentes de un ensamblado con sus 
# relaciones jerárquicas. Empiece con un producto principal formado por tres 
# sub-conjuntos los que a su vez tendrán cuatro piezas cada uno. Genere clases 
# que representen esa configuración y la muestren. Luego agregue un subconjunto opcional adicional también formado por cuatro piezas. (Use el patrón 
# composite).
class Componente:
    def mostrar(self):
        pass

class Pieza(Componente):
    def mostrar(self):
        print("Pieza")

class SubConjunto(Componente):
    def __init__(self):
        self.componentes = []

    def agregar(self, componente):
        self.componentes.append(componente)

    def mostrar(self):
        for componente in self.componentes:
            componente.mostrar()

class ProductoPrincipal(Componente):
    def __init__(self):
        self.subconjuntos = [SubConjunto() for _ in range(3)]

    def agregar_subconjunto(self, subconjunto):
        self.subconjuntos.append(subconjunto)

    def mostrar(self):
        for subconjunto in self.subconjuntos:
            subconjunto.mostrar()

class ProductoCompuesto(Componente):
    def __init__(self):
        self.componentes = []

    def agregar(self, componente):
        self.componentes.append(componente)

    def mostrar(self):
        for componente in self.componentes:
            componente.mostrar()

# 4. Implemente una clase que permita a un número cualquiera imprimir su valor, 
# luego agregarle sucesivamente.
# a. Sumarle 2.
# b. Multiplicarle por 2.
# c. Dividirlo por 3.
# Mostrar los resultados de la clase sin agregados y con la invocación anidada a 
# las clases con las diferentes operaciones. Use un patrón decorator para 
# implementar.
class Operacion:
    def __init__(self, numero):
        self.numero = numero

    def imprimir(self):
        print(self.numero)

class Sumar(Operacion):
    def imprimir(self):
        print(self.numero + 2)

class Multiplicar(Operacion):
    def imprimir(self):
        print(self.numero * 2)

class Dividir(Operacion):
    def imprimir(self):
        print(self.numero / 3)

# Uso del patrón Decorator
numero = 5
operacion = Operacion(numero)
operacion.imprimir()

operacion = Sumar(operacion.numero)
operacion.imprimir()

operacion = Multiplicar(operacion.numero)
operacion.imprimir()

operacion = Dividir(operacion.numero)
operacion.imprimir()