while (True):
    try:
        numero = int(input("Ingrese un número: "))
        resultado = "ES PRIMO"
        if numero <= 3:
            resultado = "NO ES PRIMO"
        else:
            contD = 0
            cont = 1
            while (cont <= numero):
                cont += 1
                if (numero % cont == 0):
                    contD += 1
                if contD >= 2:
                    resultado = "NO ES PRIMO"
                    break
    except ValueError:
        print("Debe ingresar un número entero válido.")
    else:
        print("El número {} {}".format(numero, resultado))
        break
    finally:
        print("Fin de búsqueda")
