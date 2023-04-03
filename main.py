import math

grau = int(input())
if grau == 1:
    print("A equação é do primeiro grau")
    a = float(input())
    if a == 0:
        print("Valor de a inválido")
    else:
        b = float(input())
        raiz = -b / a
        print("{:.2f}".format(raiz))
elif grau == 2:
    print("A equação é do segundo grau")
    a = float(input())
    if a == 0:
        print("Valor de a inválido")
    else:
        b = float(input())
        c = float(input())
        if (b*b - 4*a*c) < 0:
            print("A equação não possui raízes reais")
        elif (b*b - 4*a*c) == 0:
            print("A equação possui uma raiz real")
            raiz = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
            print("{:.2f}".format(raiz))
        elif (b*b - 4*a*c) > 0:
            print("A equação possui duas raízes reais")
            raiz1 = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
            raiz2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)
            if raiz1 > raiz2:
                print("{:.2f}".format(raiz2))
                print("{:.2f}".format(raiz1))
            else:
                print("{:.2f}".format(raiz1))
                print("{:.2f}".format(raiz2))
else:
    print("Grau inválido")