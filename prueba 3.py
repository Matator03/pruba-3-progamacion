lista_asinetos_totales=[116]

asiento_comun = (60000)
asiento_piernas = (80000)
asiento_NoReclina = (50000)
cant_asientos_comun = 100
cant_asientos_piernas = 10
cant_asientos_NoReclina = 6
compra_asiento_comun = 0
compra_asiento_piernas = 0
compra_asiento_NoReclina = 0
rut = {}
while True:
    print("(1)Comprar pasajes")
    print("(2)Mostrar ubicaciones disponibles")
    print("(3)Ver listado de pasajeros")
    print("(4)Buscar pasajeros")
    print("(5)Reasignar asiento")
    print("(6)Mostrar ganancias totales")
    print("(7)Salir")
    opcion=int(input("selecione alguna opcion "))
    if opcion == 1:
        print ("(1)asiento comun = $60.000")
        print ("(2)asiento con espacio adicinal para piernas = $80.000")
        print ("(3)asiento sin reclina = $50.000")
        print ("(4)salir")
        opcion=int(input("que pasaje desea comprar"))
        if opcion == 1:
            print("usted a comprado un pasaje comun")
            cant_asientos_comun -1
        elif opcion == 2:
            print ("usted a comprado un asientos con espacio adicional para piernas")
            cant_asientos_piernas -1
        elif opcion == 3:
            print ("usted a comprado un asiento  sin reclina")
            cant_asientos_NoReclina -1
            while True:    
                if opcion == 1:
                    for asiento_comun in compra_asiento_comun:
                        input("ingrese el rut del pasajero para seleccionar su asiento")
                elif opcion == 2:
                    for asiento_piernas in compra_asiento_piernas:
                        input("ingrese el rut del pasajero para seleccionar su asiento")
                elif opcion == 3:
                    for asiento_NoReclina in compra_asiento_NoReclina:
                      input("ingrese el rut del pasajero para seleccionar su asiento")
    if opcion == 2:
        print("mostrando ubicaciones desponibles")
    if opcion ==3:
        print(len("lista de rut", rut))
