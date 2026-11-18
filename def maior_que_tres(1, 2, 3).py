def maior_que_tres(num1, num2, num3):
    maior = num1

    if num2 > maior:
        maior = num2

    if num3 > maior:
        maior = num3
    
    return maior

print("\n=============  NÚMERO MAIOR  =============")

num1 = int(input("\nDigite o 1° número (inteiro): "))
num2 = int(input("\nDigite o 2° número (inteiro): "))
num3 = int(input("\nDigite o 3° número (inteiro): "))

resp = maior_que_tres(num1, num2, num3)

resp = print("\nO maior número é o: ", resp)
