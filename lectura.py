import os

credenciales = open("./credenciales.txt", "rt", encoding = 'utf-8')
lista = credenciales.readlines()

print(lista[0].strip())
print(lista[1])