import random

#input

print("------------------------------------------")
n = int(input("Ingrese un numero entre (1-100): "))
print("------------------------------------------")

#processing

maq = random.randint(1,100)

i = 1

while n != maq:
    if n < maq:
        print("-----------------------------")
        print("El numero a adivinar es mayor")
        print("-----------------------------")
    else:
        print("-----------------------------")
        print("El numero a adivinar es menor")
        print("-----------------------------")

    print("------------------------------------------")
    n = int(input("Ingrese un numero entre (1-100): "))
    print("------------------------------------------")

    i += 1

print("-------------------------------------------------------------------")
print(f"Felicidades ganaste, tuviste {i} intentos para adivinar el numero ")
print("-------------------------------------------------------------------")