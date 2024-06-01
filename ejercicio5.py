while (True):
    try:
        numero = int(input("Ingrese un número: "))
        resultado = "NO ES PRIMO"
        if (numero == 1, 2, 3):
            resultado = "NO ES PRIMO"
        else:
            ContD = 0
            cont = 1
            while (cont <= numero):
                cont =+ 1
                if (numero % cont == 0):
                    contD =+ 1
                if contD >= 2:
                    resultado = "ES PRIMO"
                    break
    except:
        print("Ocurrió un error!!")
    else:
        print("El número {} {}".format(numero, resultado))
        break
    finally:
        print("Fin de búsqueda")