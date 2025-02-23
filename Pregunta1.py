import threading

class MyThread(threading.Thread):
    def __init__(self, a, b):
        super(MyThread, self).__init__()  # Se usa para sobrescribir el run
        self.a = a
        self.b = b
        self.suma_total = 0  # Atributo usado para calcular la suma de los exponenciales de manera parcial

    def suma_pares(self, a, b):
        suma_funcion = (2**a) + (2**b)
        return suma_funcion

    def run(self):
        self.suma_total = self.suma_pares(self.a, self.b)
        print(f'Hilo {self.name}: suma parcial de 2^{self.a} + 2^{self.b} = {self.suma_total}')


def main():
    # Inicialización de las variables necesarias
    suma = 0
    a = 1
    b = 2
    # Lista con los hilos
    threads = []

    for i in range(5):
        t = MyThread(a, b)
        t.start()
        threads.append(t)  # Guardamos los hilos en la lista
        a += 2  # Actualizamos el valor de a
        b += 2  # Actualizamos el valor de b

    for t in threads:
        t.join()  # Esperamos a que finalicen los hilos

    for t in threads:  
        suma += t.suma_total  # Acumula la suma de los resultados de cada hilo

    print(f'La suma total es: {suma}')

if __name__ == '__main__':
    main()
