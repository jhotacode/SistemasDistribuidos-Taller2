'''
Llenar un vector de 20 posiciones(puede utilizar una lista) con números aleatorios en el rango 1-100. Utilizar 10 hilos para calcular la norma de dicho vector.
'''
import threading, math

class MyThread(threading.Thread):
    def __init__(self,a,b):
        super(MyThread,self).__init__() #Atributo para sobreescribir en el método run
        self.a = a
        self.b = b
        self.suma_norma = 0 
    
    def suma_parcial(self,a,b):
        suma = a**2 + b**2
        return suma

    def run(self):
        self.suma_norma = self.suma_parcial(self.a,self.b)
        print(f"Hilo {self.name}: La suma es: {self.suma_norma}")
        
def main():
    norma = 0
    lista_ejercicio = []
    for i in range(20):
        numero = int(input(f"Ingresa el numero {i+1} para la lista: "))    
        lista_ejercicio.append(numero)
    aux = 0
    
    threads = [] #Lista para guardar los hilos
    for i in range(10):
        a = lista_ejercicio[aux]
        b = lista_ejercicio[aux+1]
        t = MyThread(a,b) #Creamos los hilos
        t.start() #Inicializamos los hilos
        threads.append(t) #Agregamos los hilos a la lista
        aux += 2
    
    for t in threads:
        t.join()  # Esperamos a que finalicen los hilos

    for t in threads:  
        norma += t.suma_norma  # Acumula la suma de los resultados de cada hilo

    print(f'La norma del vector es: {math.sqrt(norma)}')

if __name__ == '__main__':
    main()
    
    