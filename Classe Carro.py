class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir(self):
        print(f"\nMarca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")

carro1 = Carro("Ford", "EcoSport SUV", 2018)
carro2 = Carro("Fiat", "Uno", 2008)

carro1.exibir()
carro2.exibir()