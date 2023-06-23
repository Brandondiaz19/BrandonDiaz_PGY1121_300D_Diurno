import random
opcion = 0
opcion_tipos = 0
registro_autos = []

while True:
    print("Buenos días...")
    nombre = input("Ingrese su nombre y apellido: ")
    diccionario = {"1.-":"Registrar nuevo auto a la venta","2.-":"Revisar autos registrados","3.-":"Imprimir certificados","4.-":"Salir"}
    for x, y in diccionario.items():
        print(x,y)

    print("Escoja una opcion:\n")
    
    opcion = int(input())
    print("==================================================================")
    if opcion  == 1:
        print("Ha elegido registrar un nuevo auto a la venta.")
        print("Por favor, para continuar seleccione el tipo de vehiculo que desea vender:")
        diccionario_tipos =  {"1.-":"Sedán", "2.-":"Hatchback", "3.-": "SUV", "4.-":"Station Wagon"}
        for x,y in diccionario_tipos.items():
            print(x,y)
        print("Escoja una opcion: ")
        opcion_tipos = int(input(">> "))
        print("==================================================================")
        
        if opcion_tipos == 1:
            print("Ha seleccionado Sedán,porfavor siga con los siguientes pasos")
            patente = input("Escriba la patente del vehiculo: ")
            marca = input("Escriba la marca del vehiculo: ")
            modelo = input("Escriba el modelo del vehiculo: ")
            fecha_registro =  input("Escriba la fecha en la cual este vehiculo esta siendo registrado(00/00/0000):")
            precio_auto = int(input("Escriba el precio de la venta del vehiculo: $"))
            multas_monto = int(input("Coloque el valor total de las multas que tiene el vehiculo: $"))
            multas_fechas = input("Coloque la fecha de la multa(en formato 00/00/0000):")
            nombre_dueño = input("Escriba el nombre del propietario del vehiculo:")
            auto =  {"Patente": patente,"Marca":marca, "Modelo":modelo, "Fecha de registro":fecha_registro, "Precio":precio_auto,"Monto Multas":multas_monto,"Fecha Multas":multas_fechas,"Nombre dueño":nombre_dueño}
            registro_autos.append(auto)
            print("==================================================================")
            print("El vehiculo ha sido registrado.")
            print("==================================================================")
        
        elif opcion_tipos == 2:
            print("Ha seleccionado Hatchback,porfavor siga con los siguientes pasos")
            patente = input("Escriba la patente del vehiculo: ")
            marca = input("Escriba la marca del vehiculo: ")
            modelo = input("Escriba el modelo del vehiculo: ")
            fecha_registro =  input("Escriba la fecha en la cual este vehiculo esta siendo registrado(00/00/0000):")
            precio_auto = int(input("Escriba el precio de la venta del vehiculo: $"))
            multas_monto = int(input("Coloque el valor total de las multas que tiene el vehiculo: $"))
            multas_fechas = input("Coloque la fecha de la multa(en formato 00/00/0000):")
            nombre_dueño = input("Escriba el nombre del propietario del vehiculo:")
            auto =  {"Patente": patente,"Marca":marca, "Modelo":modelo, "Fecha de registro":fecha_registro, "Precio":precio_auto,"Monto Multas":multas_monto,"Fecha Multas":multas_fechas,"Nombre dueño":nombre_dueño}
            registro_autos.append(auto)
            print("==================================================================")
            print("El vehiculo ha sido registrado.")
            print("==================================================================")
        
        elif opcion_tipos == 3:
            print("Ha seleccionado SUV,porfavor siga con los siguientes pasos")
            patente = input("Escriba la patente del vehiculo: ")
            marca = input("Escriba la marca del vehiculo: ")
            modelo = input("Escriba el modelo del vehiculo: ")
            fecha_registro =  input("Escriba la fecha en la cual este vehiculo esta siendo registrado(00/00/0000):")
            precio_auto = int(input("Escriba el precio de la venta del vehiculo: $"))
            multas_monto = int(input("Coloque el valor total de las multas que tiene el vehiculo: $"))
            multas_fechas = input("Coloque la fecha de la multa(en formato 00/00/0000):")
            nombre_dueño = input("Escriba el nombre del propietario del vehiculo:")            
            auto =  {"Patente": patente,"Marca":marca, "Modelo":modelo, "Fecha de registro":fecha_registro, "Precio":precio_auto,"Monto Multas":multas_monto,"Fecha Multas":multas_fechas,"Nombre dueño":nombre_dueño}
            registro_autos.append(auto)
            print("==================================================================")
            print("El vehiculo ha sido registrado.")
            print("==================================================================")
        
        elif opcion_tipos == 4:
            print("Ha seleccionado Station Wagon,porfavor siga con los siguientes pasos")
            patente = input("Escriba la patente del vehiculo: ")
            marca = input("Escriba la marca del vehiculo: ")
            modelo = input("Escriba el modelo del vehiculo: ")
            fecha_registro =  input("Escriba la fecha en la cual este vehiculo esta siendo registrado(00/00/0000):")
            precio_auto = int(input("Escriba el precio de la venta del vehiculo:$"))
            multas_monto = int(input("Coloque el valor total de las multas que tiene el vehiculo: $"))
            multas_fechas = input("Coloque la fecha de la multa(en formato 00/00/0000):")
            nombre_dueño = input("Escriba el nombre del propietario del vehiculo:")            
            auto =  {"Patente": patente,"Marca":marca, "Modelo":modelo, "Fecha de registro":fecha_registro, "Precio":precio_auto,"Monto Multas":multas_monto,"Fecha Multas":multas_fechas,"Nombre dueño":nombre_dueño}
            registro_autos.append(auto)
            print("==================================================================")
            print("El vehiculo ha sido registrado.")
            print("==================================================================")

    
    if opcion == 2:
        patente_buscar = input("Ingrese la patente del vehiculo: ")
        encontrado = False
        print("==================================================================")

        for auto in registro_autos:
            if auto["Patente"] == patente_buscar:
                print("Dueño: ", auto["Nombre dueño"])
                print("Marca: ", auto["Marca"])
                print("Modelo: ", auto["Modelo"])
                print("Fecha de registro: ", auto["Fecha de registro"])
                print("Precio: ", auto["Precio"])
                print("Monto Multas: ", auto["Monto Multas"])
                print("Fecha de las multas: ", auto["Fecha Multas"])
                print("==================================================================\n")

                encontrado = True
        if not encontrado:
            print("El auto no esta registrado o no se pudo encontrar.")
    
    if opcion == 3:
        print("==================================================================")
        print("IMPRIMIR CERTIFICADOS")
        diccionario_certficados = {"1.-": "Certificado de emision contaminante", "2.-":"Certificado de Anotaciones Vigentes", "3.-":"Certificado de Multas"}
        for x,y in diccionario_certficados.items():
            print(x,y)
        print("Escoja una opcion: ")
        opcion_certificados = int(input(">> "))
        print("==================================================================")
        if opcion_certificados == 1:
            patente_certificado = input("Ingrese la patente del vehiculo para el certificado: ")
            encontrado = False
            for auto in registro_autos:
                if auto["Patente"] == patente_certificado:
                    valor_certificado = random.randint(1500,3500)
                    print("Certificado de", auto["Marca"], auto["Modelo"])
                    print("Patente:", auto["Patente"])
                    print("El valor del certificado es: $", valor_certificado)
                    print("==================================================================")
                    encontrado = True
            if not encontrado:
                print("El auto no fue encontrado en el registro")
        elif opcion_certificados == 2:
            patente_certificado = input("Ingrese la patente del vehiculo para el certificado: ")
            encontrado = False
            for auto in registro_autos:
                if auto["Patente"] == patente_certificado:
                    valor_certificado = random.randint(1500,3500)
                    print("Certificado de", auto["Marca"], auto["Modelo"])
                    print("Patente:", auto["Patente"])
                    print("El valor del certificado es: $", valor_certificado)
                    print("==================================================================")
                    encontrado = True
            if not encontrado:
                print("El auto no fue encontrado en el registro")
        elif opcion_certificados == 3:
            patente_certificado = input("Ingrese la patente del vehiculo para el certificado: ")
            encontrado = False
            for auto in registro_autos:
                if auto["Patente"] == patente_certificado:
                    valor_certificado = random.randint(1500,3500)
                    print("Certificado de", auto["Marca"], auto["Modelo"])
                    print("Patente:", auto["Patente"])
                    print("El valor del certificado es: $", valor_certificado)
                    print("==================================================================")
                    encontrado = True
            if not encontrado:
                print("El auto no fue encontrado en el registro")
    if opcion == 4:
        print("Ha seleccionado salir, le deseamos un buen día, ¡hasta pronto", nombre,"!")
        print("==================================================================")
        break
    else:
        print("Opcion no valida")
        print("==================================================================")
