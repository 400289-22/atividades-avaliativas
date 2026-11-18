def calcular_area_retangulo(base, altura):
    area = base * altura
    return area

base = float(input("\nDigite a base do retângulo em cm: "))
altura = float(input("\nDigite a altura do retângulo em cm: "))

result = calcular_area_retangulo(base, altura)
print("\nA área é igual a : ", result, "cm^2\n")