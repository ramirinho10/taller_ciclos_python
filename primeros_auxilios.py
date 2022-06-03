estimulos = input("Responde a estimulos?\n")

if estimulos == "si":
    print("Valorar la necesidad de llevarlo al hospital más cercano")
else:
    print("Abrir la vía aérea")
    respira = input("Respira?\n")
    if respira == "si":
        print("Permitirle posición de suficiente ventilación")
    else:
        print("Administrar 5 ventilaciones y llamar a ambulancia")
        signos = input("Signos de vida?\n")
        if signos == "si":
            print("Reevaluar a la espera de la Ambulancia")
            ambulancia = input("Llego la ambulancia?\n")
            while ambulancia != "si":
                signos = input("Signos de vida?\n")
                if signos == "si":
                    print("Reevaluar a la espera de la Ambulancia")
                    ambulancia = input("Llego la ambulancia?\n")
                else:
                    print("Administar Compresiones Toracicas hasta que llegue la ambulancia")
                    ambulancia = input("Llego la ambulancia?\n")
        else:
            print("Administar Compresiones Toracicas hasta que llegue la ambulancia")  
            ambulancia = input("Llego la ambulancia?\n")
            while ambulancia != "si":
                signos = input("Signos de vida?\n")
                if signos == "si":
                    print("Reevaluar a la espera de la Ambulancia")
                    ambulancia = input("Llego la ambulancia?\n")
                else:
                    print("Administar Compresiones Toracicas hasta que llegue la ambulancia")
                    ambulancia = input("Llego la ambulancia?\n")

print("FIN")
