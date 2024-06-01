while (True):
    try:
        numero = int(input("Ingrese un año: "))
        resultado = "NO ES BISIESTO"
        if (numero % 4 == 0 and numero % 100 != 0) or (numero % 400 == 0):
            resultado = "ES BISIESTO"
        print("El año {} {}".format(numero, resultado))
        break
    except:
        print("Ocurrió un error!!")
#    else:
#        print("El año {} {}".format(numero, resultado))
#        break
#    finally:
#        print("Fin de búsqueda")