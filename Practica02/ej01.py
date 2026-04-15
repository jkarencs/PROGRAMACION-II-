# TAREA DE KAREN JEANETTE CARRILLO SALINAS 
# PRACTICA 2 : EJERCICIO 1

# EJERCICIO 1: La clase MiPunto. Dise˜ne una clase llamada MiPunto para representar un punto con
# coordenadas x e y. La clase contiene:
    # a) Los atributos x e y que representan las coordenadas con m´etodos getter.
    # b) Un constructor sin argumentos que crea un punto (0, 0).
    # c) Un constructor que construye un punto con las coordenadas especificadas. 
    # d) Un m´etodo llamado distancia que retorna la distancia desde este punto hasta un
      # punto especificado del tipo MiPunto.
    # e) Un m´etodo llamado distancia que retorna la distancia desde este punto hasta otro
      # punto con las coordenadas x e y especificadas.
#Dibuje el diagrama UML de la clase e implem´entela. Escriba un programa de prueba que
#cree los puntos (0, 0) y (10, 30.5) y muestre la distancia entre ellos.

# -------- codigo --------

import math
class MiPunto:
    # b) y c) CONSTRUCTORES
    def __init__(self, x=0, y=0):
        self.__x = x 
        self.__y = y
    # a) METODOS GETTER
    
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    # d) METODO DISTANCIA CON PUNTO ESPECIFICADO
    # uso *args  para q vengan varios argumentos.
    def distancia(self, *args):
        if len(args) == 1:
            otro = args [0]
            dx = self.__x - otro.get_x()
            dy = self.__y - otro.get_y()
            
    # e)Si mandas dos número 

        elif len(args) == 2:
            x_externa = args[0]
            y_externa = args[1]
            dx = self.__x - x_externa
            dy = self.__y - y_externa
            
        return math.sqrt(dx**2 + dy**2)


p1 = MiPunto()           
p2 = MiPunto(10, 30.5)  
dist = p1.distancia(p2)   
print(f"------resultados------")
print(f"El punto 1 es: ({p1.get_x()}, {p1.get_y()})")
print(f"El punto 2 es: ({p2.get_x()}, {p2.get_y()})")
print(f"La distancia entre los puntos es: {dist:.2f}")