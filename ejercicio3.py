while (True):
    try:
        numero = int(input("Ingrese un número: "))
        resultado = "IMPAR"
        if (numero % 2 == 0):
            resultado = "PAR"
        print("El número {} es {}".format(numero, resultado))
        break
    except:
        print("Ocurrió un error!!")