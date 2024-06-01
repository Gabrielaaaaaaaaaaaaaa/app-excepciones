from operaciones.calculadora import *
num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")
print ("{} + {} = {}".format(num1, num2, sumar(num1, num2)))
print ("{} - {} = {}".format(num1, num2, restar(num1, num2)))
print ("{} * {} = {}".format(num1, num2, multiplicar(num1, num2)))
print ("{} / {} = {}".format(num1, num2, dividir(num1, num2)))