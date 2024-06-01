def sumar(numero1, numero2):
    try:
        resultado = int(numero1) + int(numero2)
    except:
        print("Ingrese solo números")
    else:
        return resultado

def restar(numero1, numero2):
    try:
        resultado = int(numero1) - int(numero2)
    except:
        print("Ingrese solo números")
    else:
        return resultado

def multiplicar(numero1, numero2):
    try:
        resultado = int(numero1) * int(numero2)
    except:
        print("Ingrese solo números")
    else:
        return resultado

def dividir(numero1, numero2):
    try:
        resultado = int(numero1) / int(numero2)
    except ValueError:
        print("Ingrese solo números")
    except ZeroDivisionError:
        print("El número no puede ser divisible entre 0")
    else:
        return resultado