class Figura:
    def __init__(self):
        pass

class Retangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = self.base * self.altura

    def calcular_area(self):
        print(f"\nA área do retângulo é igual a: {self.area} ")
        print("="*40)

print("\n--------- ÁREA DO RETÂNGULO ----------")

b = float(input("Digite o valor da base do retângulo: "))
h = float(input("\nDigite o valor da altura do retângulo: "))

r1 = Retangulo(b,h)
r1.calcular_area()

class Circulo(Figura):
    def __init__(self, raio):
        self.raio = raio
        self.pi = 3.14
        
    def calcular_area_c(self):
        self.area = self.pi * (self.raio ** 2)
        print(f"\nA área do círculo é igual a: {self.area}")
        print("="*40)

print("\n--------- ÁREA DO CÍRCULO ---------")

a = float(input("\nDigite o raio do círculo: "))

c1 = Circulo(a)
c1.calcular_area_c()