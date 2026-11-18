print("\n=================== CONVERSOR PYTHON ===================\n")

while True:
    print("1 - Converter de Celsius para Fahrenheit")
    print("2 - Converter de Fahrenheit para Celsius")
    print("3 - Converter de Km para Milhas")
    print("4 - Converter de KG para Libras")
    print("5 - Converter de Metros para Centímetros")
    print("0 - Sair do programa\n")

    opcao = int(input("Escolha uma das opções: "))

    if opcao == 1:
        celsius = float(input("\nDigite a temperatura em Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C é igual a {fahrenheit:.2f}°F\n")

    elif opcao == 2:
        fahrenheit = float(input("\nDigite a temperatura em Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F é igual a {celsius:.2f}°C\n")
    
    elif opcao == 3:
        km = float(input("\nDigite a distância em Km: "))
        milhas = km / 1.609
        print(f"{km} Km é igual a {milhas:.2f} Milhas\n")
    
    elif opcao == 4:
        kg = float(input("\nDigite o peso em KG: "))
        libras = kg * 2.20462
        print(f"{kg} KG é igual a {libras:.2f} Libras\n")
    
    elif opcao == 5:
        metros = float(input("\nDigite o comprimento em Metros: "))
        centimetros = metros * 100
        print(f"{metros} Metros é igual a {centimetros:.2f} Centímetros\n")
    
    elif opcao == 0:
        print("\nSaindo do programa...")
        break
    else:
        print("\nOpção inválida. Por favor, escolha uma opção válida.\n")
        continue