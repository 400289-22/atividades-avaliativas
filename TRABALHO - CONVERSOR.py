print("\n=================== CONVERSOR PYTHON ===================\n")


def cel_far(temp):
        fahrenheit = (temp * 9/5) + 32
        return fahrenheit

def far_cel(temp): 
        celsius = (temp - 32) * 5/9
        return celsius

def km_milhas(distancia):
    milhas = distancia / 1.609
    return milhas

def kg_libras(peso):
    libras = peso * 2.20462
    return libras

def metros_centimetros(comprimento):
    centimetros = comprimento * 100
    return centimetros

while True:
    print("1 - Converter de Celsius para Fahrenheit")
    print("2 - Converter de Fahrenheit para Celsius")
    print("3 - Converter de Km para Milhas")
    print("4 - Converter de KG para Libras")
    print("5 - Converter de Metros para Centímetros")
    print("0 - Sair do programa\n")

    opcao = int(input("Escolha uma das opções: "))






    if opcao == 1:
        print("\nEssa função converte celsius para fahrenheit\n")
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = cel_far(celsius)
        print(f"{celsius}°C é igual a {fahrenheit:.2f}°F\n")

    elif opcao == 2:
        print("\nEssa função converte fahrenheit para celsius\n")
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = far_cel(fahrenheit)
        print(f"{fahrenheit}°F é igual a {celsius:.2f}°C\n")
    
    elif opcao == 3:
        print("\nEssa função converte km para milhas\n")
        km = float(input("Digite a distância em Km: "))
        milhas = km_milhas(km)
        print(f"{km} Km é igual a {milhas:.2f} Milhas\n")
    
    elif opcao == 4:
        print("\nEssa função converte kg para libras\n")
        kg = float(input("Digite o peso em KG: "))
        libras = kg_libras(kg)
        print(f"{kg} KG é igual a {libras:.2f} Libras\n")
    
    elif opcao == 5:
        print("\nEssa função converte metros para centímetros\n")
        metros = float(input("Digite o comprimento em Metros: "))
        centimetros = metros_centimetros(metros)
        print(f"{metros} Metros é igual a {centimetros:.2f} Centímetros\n")
    
    elif opcao == 0:
        print("\nSaindo do programa...")
        break
    else:
        print("\nOpção inválida. Por favor, escolha uma opção válida.\n")
        continue