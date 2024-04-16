#1. Provea una clase que dado un número entero cualquiera retorne el factorial del mismo, debe asegurarse que todas las clases que lo invoquen utilicen la misma 
#instancia de clase
class FactorialCalculator:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def calculate_factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.calculate_factorial(n-1)

factorial_calculator = FactorialCalculator()
print(factorial_calculator.calculate_factorial(5)) 

#2. Elabore una clase para el cálculo del valor de impuestos a ser utilizado por 
# todas las clases que necesiten realizarlo. El cálculo de impuestos simplificado 
# deberá recibir un valor de importe base imponible y deberá retornar la suma 
# del cálculo de IVA (21%), IIBB (5%) y Contribuciones municipales (1,2%) sobre 
# esa base imponible.
class TaxCalculator:
    @staticmethod
    def calculate_taxes(base_amount):
        iva = base_amount * 0.21
        iibb = base_amount * 0.05
        municipal_contributions = base_amount * 0.012
        total_taxes = iva + iibb + municipal_contributions
        return total_taxes

tax_amount = TaxCalculator.calculate_taxes(1000)  
print("Total de impuestos a pagar:", tax_amount)

# 3. Genere una clase donde se instancie una comida rápida “hamburguesa” que 
# pueda ser entregada en mostrador, retirada por el cliente o enviada por 
# delivery. A los efectos prácticos bastará que la clase imprima el método de 
# entrega.
class FastFood:
    def __init__(self, food_name):
        self.food_name = food_name

    def delivery(self):
        print(f"{self.food_name} - Entrega a domicilio")

    def pickup(self):
        print(f"{self.food_name} - Retirar en el local")

burger = FastFood("Hamburguesa")
burger.delivery()

# 4.Implemente una clase “factura” que tenga un importe correspondiente al total 
# de la factura pero de acuerdo a la condición impositiva del cliente (IVA 
# Responsable, IVA No Inscripto, IVA Exento) genere facturas que indiquen tal 
# condición. 
class Factura:
    def __init__(self, importe, tipo_iva):
        self.importe = importe
        self.tipo_iva = tipo_iva
    
    def generar_factura(self):
        if self.tipo_iva == "Responsable":
            return f"Factura: ${self.importe} (IVA Responsable)"
        elif self.tipo_iva == "No Inscripto":
            return f"Factura: ${self.importe} (IVA No Inscripto)"
        elif self.tipo_iva == "Exento":
            return f"Factura: ${self.importe} (IVA Exento)"

factura_responsable = Factura(1000, "Responsable")
print(factura_responsable.generar_factura())  

factura_no_inscripto = Factura(1500, "No Inscripto")
print(factura_no_inscripto.generar_factura())  
factura_exento = Factura(800, "Exento")
print(factura_exento.generar_factura()) 

# 5. Extienda el ejemplo visto en el taller en clase de forma que se pueda utilizar 
# para construir aviones en lugar de vehículos. Para simplificar suponga que un 
# avión tiene un “body”, 2 turbinas, 2 alas y un tren de aterrizaje.
class Airplane:
    def __init__(self):
        self.body = "Cuerpo"
        self.engines = 2
        self.wings = 2
        self.landing_gear = "Tren de aterrizaje"

airplane = Airplane()
print(f"Avión: {airplane.body}, Turbinas: {airplane.engines}, Alas: {airplane.wings}, Tren de aterrizaje: {airplane.landing_gear}")

# 6. Extienda el ejemplo del taller para prototipos de forma que genere 20 
# anidamientos y que la carga simulada de procesamiento dure 2 segundos.
import time

class Prototype:
    def __init__(self, depth):
        self.depth = depth

    def process(self):
        if self.depth > 0:
            print(f"Procesando nivel {self.depth}")
            time.sleep(2)  
            Prototype(self.depth - 1).process()

Prototype(20).process()

