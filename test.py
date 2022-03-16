# Numeros a validar
def capt_num():
    n: int = int(input("Cantidad de elementos a validar"))
    if n <= 0:
        print("Debe ser un numero mayor a 0")
        capt_num()
    else:
        num_list = np.random.randint(1, n, n)
    return validacion(num_list)


def validacion(num_list):
    muestra: list = num_list
    print(f"A continuación se presenta la muestra a examinar: \n{[muestra]}")
    for e in muestra:
        if e < 0:
            print("Factorial of negative e does not exist")
        elif e == 0:
            return 1
        else:
            fact = 1
            while(e > 1):
                fact *= e
                e -= 1
            return fact
    if fact % 2 != 0:
        print(f"El numero {e} es un numero inteligente")
    else:
        print(f"El numero {e} no un numero inteligente")
