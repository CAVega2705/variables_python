# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese tres palabras y arme un acrónimo con ellas
# Si desea puede modificar el código para ingresar más palabras
print('Ingrese palabra 1:')
palabra_1 = str(input())
#Asociacion
print('Ingrese palabra 2:')
palabra_2 = str(input())
#Futbol
print('Ingrese palabra 3:')
palabra_3 = str(input())
#Argentino
# De cada palabra debe tomar la primera letra y armar el acrónimo
# Ejemplo: Alumbrado, barrido y limpieza --> ABL
# Imprimir el resultado en pantalla
caracter_inicial_1 = palabra_1 [0]
caracter_inicial_2 = palabra_2 [0]
caracter_inicial_3 = palabra_3 [0]
print("El acrónimo formado es:", caracter_inicial_1 + "." + caracter_inicial_2 + "." + caracter_inicial_3 + ".")
