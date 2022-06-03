#python fuerza_bruta.py
#Ingrese la contraseña: gato

from string import ascii_lowercase
import getpass

password = getpass.getpass("Ingrese su contraseña: ")

abecedario = ascii_lowercase

contador = 0

for letra in password:
    for caracter in abecedario:
        contador += 1
        if letra == caracter:
            break
    
print(f"La contraseña {password} fue forzada en {contador} intentos")