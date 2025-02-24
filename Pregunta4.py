import threading
import math

class MyThread(threading.Thread):
    def __init__(self, start, end):
        super(MyThread, self).__init__()
        self.start_num = start
        self.end_num = end
        self.suma_factoriales = 0
        
    def factorial(self, n):
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact
    
    def run(self):
        for i in range(self.start_num, self.end_num + 1):
            self.suma_factoriales += self.factorial(i)

def main():
    suma_funcion = 0
    n = int(input("Ingresa el valor de n: "))
    num_hilos = int(input("Número de hilos: "))

    if n < num_hilos:
        print("Se está realizando un proceso poco óptimo")
        num_hilos = n  # Limitar el número de hilos al valor de n

    threads = []
    rango = math.ceil(n / num_hilos)

    for i in range(num_hilos):
        start = i * rango + 1
        end = min((i + 1) * rango, n)

        t = MyThread(start, end)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
        suma_funcion += t.suma_factoriales  # Sumar resultados de cada hilo

    print(f"Suma de los factoriales: {suma_funcion}")

if __name__ == '__main__':
    main()
