import sys

ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}


filtro = int(sys.argv[1])

"""
#1) #Metodo 1
filtro = int(sys.argv[1])

ventas_filtro = {}

for clave, valor in ventas.items():
    if valor > filtro:
        ventas_filtro[clave] = valor

print(ventas_filtro)
"""

#2) #Metodo 2

filtro = int(sys.argv[1])

print({k:v for k, v in ventas.items() if v>filtro})
