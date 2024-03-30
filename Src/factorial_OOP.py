class Factorial:
    def __init__(self, min_num, max_num):
        self.min_num = min_num
        self.max_num = max_num

    def calcular_factorial(self, num):
        if num < 0:
            print("El factorial de un número negativo no existe")
            return None
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

    def run(self):
        for num in range(self.min_num, self.max_num + 1):
            print("El factorial de", num, "! es", self.calcular_factorial(num))

if __name__ == "__main__":
    min_num = int(input("Ingrese el número mínimo del rango: "))
    max_num = int(input("Ingrese el número máximo del rango: "))

    factorial_calculator = Factorial(min_num, max_num)
    factorial_calculator.run()