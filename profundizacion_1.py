# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

numero_1 = float(input("ingrese un número:"))
numero_2 = float(input("ingrese otro número:"))

suma = numero_1 + numero_2
resta = numero_1 + numero_2
multiplicacion = numero_1 * numero_2
division = numero_1 / numero_2
exponente = numero_1 ** numero_2

print("La suma entre {} y {} es {}".format(numero_1, numero_2, suma))
print("si a {} le restamos {} da como resultado {}".format(numero_1, numero_2, resta))
print("la multiplicación entre {} y {} es {}".format(numero_1, numero_2, multiplicacion))
print("{} dividido {} da como resultado {}".format(numero_1, numero_2, division))
print("{} elevado a {} da como resultado {}".format(numero_1, numero_2, exponente))
