import matplotlib.pyplot as plt

def collatz(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count

def main():
    x_values = []
    y_values = []
    for i in range(1, 10001):
        x_values.append(i)
        y_values.append(collatz(i))

    plt.scatter(y_values, x_values, marker='o', color='blue', s=5)
    plt.title('Número de Collatz para los números entre 1 y 10000')
    plt.xlabel('Número de iteraciones')
    plt.ylabel('Número inicial de la secuencia')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()