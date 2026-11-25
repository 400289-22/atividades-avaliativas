class Veiculo:
    def __init__(self, marca, velocidade_max):
        self.marca = marca
        self.velocidade_max = velocidade_max

    def mover(self):
        print(f"O veículo {self.marca} está se movendo..")

class Carro(Veiculo):
    def __init__(self, marca, velocidade_max, num_portas):
        super().__init__(marca, velocidade_max)
        self.num_portas = num_portas
        
    def exibir(self):
        print("\n----------- CARRO ----------")
        print(f"Marca: {self.marca}")
        print(f"Velocidade Máxima: {self.velocidade_max}")
        print(f"Número de Portas: {self.num_portas}")

class Bicicleta(Veiculo):
    def __init__(self, marca, velocidade_max, num_marchas):
        super().__init__(marca, velocidade_max)
        self.num_marchas = num_marchas
    
    def exibir_1(self):
        print("\n--------- BICICLETA ---------")
        print(f"Marca: {self.marca}")
        print(f"Velocidade Máxima: {self.velocidade_max}")
        print(f"Número de Marchas: {self.num_marchas}")

carro = Carro("Tucson", "200 Km/h", 5)
bicicleta = Bicicleta("Caloi", "40 Km/h", 7)

carro.exibir()
carro.mover()

bicicleta.exibir_1()
bicicleta.mover()
