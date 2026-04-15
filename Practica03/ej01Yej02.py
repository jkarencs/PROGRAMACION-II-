#POR KAREN JEANETTE CARRILLO SALINAS
#Practica 3 - herencia
#Clase Juego 1 y 2 
#EJERCICIO N°1 y 2 en uno solo 
#clase juego 
class Juego:
    def __init__(self, num_vidas , record):
        self.numeroDeVidas = num_vidas
        self.vidasIniciales = num_vidas
        self.record = record

    def reiniciaPartida(self):
        self.numeroDeVidas = self.vidasIniciales


    def actualizaRecord(self):
        self.record += 1
        print("Nuevo record:", self.record)

    def quitaVida(self):
        self.numeroDeVidas -= 1
        print("Te quedan", self.numeroDeVidas, "vidas")
        if self.numeroDeVidas > 0:
            return True  
        else:
            print("GAME OVER")
            return False 
        
#******************************************
#          ejercicio 1 union con ejer. 2
#******************************************

import random
class JuegoAdivinaNumero(Juego):
    def __init__(self, num_vidas):
        super().__init__(num_vidas, record = 0)
        self.numeroAAdivinar = 0

    def validaNumero(self, numero):
        if numero >= 0 and numero <= 10:
            return True
        else:
            return False
    #JUEGO PRINCIPAL
    def juega(self):
        self.reiniciaPartida()

        # Genera número aleatorio entre 0 y 10
        self.numeroAAdivinar = random.randint(0, 10)

        print("Adivina un número entre 0 y 10")
        
        #bucle infinito hasta q gane o pierda
        while True:

            intento = int(input("Ingresa tu número: "))

            if intento == self.numeroAAdivinar:
                print("Acertaste ")
                self.actualizaRecord()
                break

            else:
                sigue = self.quitaVida()

                if sigue == True:
                    if intento < self.numeroAAdivinar:
                        print("El número es mayor")
                    else:
                        print("El número es menor")

                    print("Intenta de nuevo...")

                else:
                    print("El número era:", self.numeroAAdivinar)
                    break

#*****************************************
# Parte del ejer.2 par-impar
#*****************************************
class JuegoAdivinaPar(JuegoAdivinaNumero):

    def validaNumero(self, numero):

        if numero >= 0 and numero <= 10:
            if numero % 2 == 0:
                return True
            else:
                print("Error: el número debe ser PAR")
                return False
        else:
            return False
    def juega(self):
        self.reiniciaPartida()

        self.numeroAAdivinar = random.choice([0,2,4,6,8,10])

        print("Adivina un número PAR entre 0 y 10")

        while True:
            intento = int(input("Ingresa tu número: "))

            if self.validaNumero(intento) == False:
                continue

            if intento == self.numeroAAdivinar:
                print("Acertaste")
                self.actualizaRecord()
                break
            else:
                sigue = self.quitaVida()

                if sigue:
                    if intento < self.numeroAAdivinar:
                        print("El número es mayor")
                    else:
                        print("El número es menor")
                else:
                    print("El número era:", self.numeroAAdivinar)
                    break
        
        
class JuegoAdivinaImpar(JuegoAdivinaNumero):

    def validaNumero(self, numero):
        

        if numero >= 0 and numero <= 10:
            if numero % 2 != 0:
                return True
            else:
                print("Error: el número debe ser IMPAR")
                return False
        else:
            return False
    def juega(self):
        self.reiniciaPartida()

        self.numeroAAdivinar = random.choice([1,3,5,7,9])

        print("Adivina un número IMPAR entre 0 y 10")

        while True:
            intento = int(input("Ingresa tu número: "))

            if self.validaNumero(intento) == False:
                continue

            if intento == self.numeroAAdivinar:
                print("Acertaste")
                self.actualizaRecord()
                break
            else:
                sigue = self.quitaVida()

                if sigue:
                    if intento < self.numeroAAdivinar:
                        print("El número es mayor")
                    else:
                        print("El número es menor")
                else:
                    print("El número era:", self.numeroAAdivinar)
                    break

#Main uwu 
print("Bienvenido al juego de adivinar el número")
print("----- Juego Normal -----")
j1 = JuegoAdivinaNumero(3)
j1.juega()

print("\n----- Juego PAR -----")
j2 = JuegoAdivinaPar(3)
j2.juega()

print("\n----- Juego IMPAR -----")
j3 = JuegoAdivinaImpar(3)
j3.juega()