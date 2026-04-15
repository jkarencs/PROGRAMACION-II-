import math

class Vector3D:

    # Constructor
    def __init__(self, a1=0, a2=0, a3=0):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    # a) Suma de vectores
    def __add__(self, otro):
        return Vector3D(
            self.a1 + otro.a1,
            self.a2 + otro.a2,
            self.a3 + otro.a3
        )

    # b) Multiplicación (polimorfismo)
    def __mul__(self, otro):

        # escalar
        if isinstance(otro, (int, float)):
            return Vector3D(
                self.a1 * otro,
                self.a2 * otro,
                self.a3 * otro
            )

        # producto escalar
        elif isinstance(otro, Vector3D):
            return (
                self.a1 * otro.a1 +
                self.a2 * otro.a2 +
                self.a3 * otro.a3
            )

    # c) Módulo del vector
    def modulo(self):
        return math.sqrt(
            self.a1**2 + self.a2**2 + self.a3**2
        )

    # d) Vector unitario (normal)
    def normal(self):
        mod = self.modulo()
        return Vector3D(
            self.a1 / mod,
            self.a2 / mod,
            self.a3 / mod
        )

    # e) Producto vectorial
    def cruz(self, otro):
        return Vector3D(
            self.a2 * otro.a3 - self.a3 * otro.a2,
            self.a3 * otro.a1 - self.a1 * otro.a3,
            self.a1 * otro.a2 - self.a2 * otro.a1
        )

    # Mostrar
    def __str__(self):
        return "({}, {}, {})".format(self.a1, self.a2, self.a3)
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

print("Vector 1:", v1)
print("Vector 2:", v2)

print("Suma:", v1 + v2)
print("Escalar:", v1 * 2)
print("Producto escalar:", v1 * v2)
print("Módulo:", v1.modulo())
print("Normal:", v1.normal())
print("Producto vectorial:", v1.cruz(v2))