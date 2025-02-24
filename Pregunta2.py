'''
Implemente en una clase los métodos: suma, resta, multiplicación y división. Todos
los métodos reciben 2 argumentos, en el método “RUN” se deben ejecutar 1
operación. Lanzar todas las operaciones con 4 hilos(puede modificar el constructor
como quiera)
'''

import threading

class MyThreading(threading.Thread):
    def __init__(self,x,y,operation):
        super(MyThreading,self).__init__()
        self.x = x
        self.y = y
        self.operation = operation #Variable para decidir la operación
        self.result = None #Variable para almacenar el resultado
        
    def suma(self):
        return self.x + self.y
    def resta(self):
        return self.x - self.y
    def multiplicacion(self):
        return self.x * self.y
    def division(self):
        if self.y != 0:
            return self.x / self.y
        else:
            return None
        
    def run(self):
        if self.operation == 1:
            self.result = self.suma()
        elif self.operation == 2:
            self.result = self.resta()
        elif self.operation == 3:
            self.result = self.multiplicacion()
        elif self.operation == 4:
            self.result = self.division()
                
def main():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    operations = [1,2,3,4]
    threads = [] #Lista de hilos
    result = {}
    
    for operation in operations:
        t = MyThreading(num1,num2,operation)
        t.start()
        threads.append(t)
        
    for t in threads:
        t.join()
        result[t.operation] = t.result
    
    # Imprimir resultados
    print(f"Suma: {result[1]}")
    print(f"Resta: {result[2]}")
    print(f"Multiplicación: {result[3]}")
    print(f"División: {result[4]}")
    
if __name__ == '__main__':
    main()
    