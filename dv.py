"""python dv.py
Ingresa tu RUT sin puntos ni dígito verificador: 12345678
Su dígito verificador es 5"""

import math

serie = [2, 3, 4, 5, 6, 7]
serie *= 2

#print(serie) 

#Ejercicio invertir rut

rut = input("Ingrese su rut sin digito vertificador ni puntos: ")

rut_invertido = rut[::-1]

largo = len(rut_invertido)

#Revision de rut x serie

resultado_rut = [int(n) * d for d, n in zip(serie[:largo], rut_invertido)]

#Suma

suma = sum(resultado_rut)

#modulo11

mod_11 = int(suma/11)

#Resto

resto = suma - mod_11 * 11

#Digito Verificador

if (11 - resto) == 10:
    dv = "k"
elif (11 - resto) == 11:
    dv = 0
else:
    dv = 11-resto

print(f"Su digito verificador es {dv}")


