class NumeroComplejo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def __add__(self, otro):
        real = self.real + otro.real
        imaginario = self.imaginario + otro.imaginario
        return NumeroComplejo(real, imaginario)

    def __sub__(self, otro):
        real = self.real - otro.real
        imaginario = self.imaginario - otro.imaginario
        return NumeroComplejo(real, imaginario)

    def __mul__(self, otro):
        real = self.real * otro.real - self.imaginario * otro.imaginario
        imaginario = self.real * otro.imaginario + self.imaginario * otro.real
        return NumeroComplejo(real, imaginario)

    def __truediv__(self, otro):
        denominador = otro.real**2 + otro.imaginario**2
        real = (self.real * otro.real + self.imaginario * otro.imaginario) / denominador
        imaginario = (self.imaginario * otro.real - self.real * otro.imaginario) / denominador
        return NumeroComplejo(real, imaginario)

    def __str__(self):
        return f"{self.real} + {self.imaginario}i"


# Ejemplo de uso
complejo1 = NumeroComplejo(3, 2)
complejo2 = NumeroComplejo(1, 7)

suma = complejo1 + complejo2
resta = complejo1 - complejo2
multiplicacion = complejo1 * complejo2
division = complejo1 / complejo2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

