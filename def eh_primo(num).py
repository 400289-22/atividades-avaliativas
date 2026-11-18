
def eh_primo(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


print("\n============= NÚMEROS PRIMOS =============")

for num in range(1, 101):
    if eh_primo(num):
        print(num)
