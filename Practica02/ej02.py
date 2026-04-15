# TAREA DE KAREN JEANETTE CARRILLO SALINAS 
# PRACTICA 2 : EJERCICIO 2

# EJERCICIO 2: Algebra Vectorial. Se quiere construir un programa orientado a objetos con sobrecarga de funciones. Para la soluci´on del problema se debe dibujar el diagrama de clases, acompa˜nado del respectivo c´odigo de soluci´on.
#El programa debe: (1) determinar si dos vectores son perpendiculares
#(2) determinar si dos vectores son paralelos
#(3) determinar la proyecci´on de dos vectores
# (4) determinar el componente de dos vectores. Para ello genere la clase AlgebraVectorial con la sobrecarga de constructores y sobrecargando los siguientes m´etodos:
#------------ metodos  -----------------
#a) Perpendicular. Si el vector a es ortogonal o perpendicular a b: |a + b| = |a − b|
#b) Perpendicular. Si el vector a es mutuamente ortogonal a b: |a − b| = |b − a|
#c) Perpendicular. Si el vector a es ortogonal a b: a · b = 0
#d) Perpendicular. Si el vector a es ortogonal a b: |a + b|^2 = |a|^2 + |b|^2
#e) Paralela. Si el vector a es paralela a b: a = rb
#f) Paralela. Si el vector a es paralela a b: a × b = 0
#g) Proyeccion de a sobre b. La proyecci´on ortogonal de a sobre b: Proyb a =a · b/(|b|elevado 2 )*b
#h) Componente de a en b. El componente de a en la direcci´on de b: Compb a =a · b / |b|


# -------- codigo --------

from multimethod import multimethod
import math

# Clase para representar un vector en 3D
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    # Sobrecarga de operadores para facilitar cálculos internos 
    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y, self.z + otro.z)

    def __sub__(self, otro):
        return Vector(self.x - otro.x, self.y - otro.y, self.z - otro.z)

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

class AlgebraVectorial:
    
    # sobre carga de metodos para determinar si son perpendiculares
    
    # Caso c): Producto punto a · b = 0
    @multimethod
    def perpendicular(self, a: Vector, b: Vector):
        dot_product = (a.x * b.x) + (a.y * b.y) + (a.z * b.z)
        return math.isclose(dot_product, 0.0, abs_tol=1e-9)

    # Caso a) y d): Según parámetros adicionales
    @multimethod
    def perpendicular(self, a: Vector, b: Vector, metodo: str):
        if metodo == "normas": # |a + b| = |a - b|
            return math.isclose((a + b).magnitud(), (a - b).magnitud())
        elif metodo == "pitagoras": # |a + b|^2 = |a|^2 + |b|^2
            return math.isclose((a + b).magnitud()**2, a.magnitud()**2 + b.magnitud()**2)
        return False

    # son paralelos si a = r*b o a × b = 0 ( e y f)
    
    # e) Si a es paralelo a b: a = rb
    def paralela(self, a: Vector, b: Vector):
        # Evitamos división por cero y comparamos razones
        componentes = [(a.x, b.x), (a.y, b.y), (a.z, b.z)]
        razones = [comp[0]/comp[1] for comp in componentes if comp[1] != 0]
        return all(math.isclose(r, razones[0]) for r in razones) if razones else True

    # g y h) Proyección y componente de a en b
    def proyeccion_de_a_sobre_b(self, a: Vector, b: Vector):
        punto = (a.x * b.x) + (a.y * b.y) + (a.z * b.z)
        factor = punto / (b.magnitud()**2)
        return Vector(factor * b.x, factor * b.y, factor * b.z)

    # h) Componente de a en b
    def componente_de_a_en_b(self, a: Vector, b: Vector):
        punto = (a.x * b.x) + (a.y * b.y) + (a.z * b.z)
        return punto / b.magnitud()

alg = AlgebraVectorial()
v1 = Vector(3.0, 4.0, 0.0)
v2 = Vector(-4.0, 3.0, 0.0) # Vector perpendicular a v1

print("Vector 1:", v1)
print("Vector 2:", v2)

print("¿Son perpendiculares (P. Punto)?", alg.perpendicular(v1, v2))
print("¿Son perpendiculares (Normas)?", alg.perpendicular(v1, v2, "normas"))

v3 = Vector(6.0, 8.0, 0.0) # Vector paralelo a v1 (v3 = 2 * v1)
print("¿v1 y v3 son paralelos?", alg.paralela(v1, v3))

print("Componente de v1 en v3:", alg.componente_de_a_en_b(v1, v3))
print("Proyección de v1 sobre v3:", alg.proyeccion_de_a_sobre_b(v1, v3))