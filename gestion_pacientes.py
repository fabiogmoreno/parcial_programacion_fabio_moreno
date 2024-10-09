from validacion import ingresar_numeros
from pacientes import pacientes as lista_pacientes
from cargar import cargar_pacientes
from mostrar import mostrar_maximo_internacion, mostrar_minimo_internacion, mostrar_pacientes
from buscar import buscar_pacientes
from ordenar import ordenar_pacientes
from calcular import contar_pacientes_5_dias,calcular_promedio_internacion
Entrar = True

while Entrar:
    print('''\t\t\tSistema de Gestion de Clinica:
            \t\t1) Cargar paciente/s
            \t\t2) Mostrar todos los pacientes
            \t\t3) Buscar pacientes por numero de Historia Clinica 
            \t\t4) Ordenar paciente por numero de Historia clinica 
            \t\t5) Mostrar paciente con mas dias de internacion
            \t\t6) Mostrar paciente con menos dias de internacion
            \t\t7) Cantidad de paciente con mas de 5 dias de inernacion
            \t\t8) Promedio de dias de internacion de todos los pacientes
            \t\t9) Salir
    ''')
     
    opcion_menu = ingresar_numeros('Ingrese una opcion: ',1,9,4)

    if opcion_menu == 1: 

        cantidad_paciente = ingresar_numeros('Ingrese la cantidad de paciente para cargar en el sistemas: ',1,100,5)
        lista_pacientes = cargar_pacientes(lista_pacientes,cantidad_paciente)

    elif opcion_menu == 2:
        
        mostrar_pacientes(lista_pacientes)

    elif opcion_menu == 3:

        pregunta_historia_clinica = ingresar_numeros('Ingrese una historia clinicia para buscar: ',1,500,3)
        buscar_pacientes(lista_pacientes,pregunta_historia_clinica)

    elif opcion_menu == 4:

       lista_pacientes = ordenar_pacientes(lista_pacientes)

    elif opcion_menu == 5:

        mostrar_maximo_internacion(lista_pacientes)

    elif opcion_menu == 6:

        mostrar_minimo_internacion(lista_pacientes)

    elif opcion_menu == 7:

        cantidad_paciente = contar_pacientes_5_dias(lista_pacientes) 

        if cantidad_paciente > 0:
            print(f'La cantidad de paciente con mayor a 5 dias de internacion es : {cantidad_paciente}')
        else:
            print('No hay cliente con mayor a esa cantidad')

    elif opcion_menu == 8:
         
        promedio_internacion = calcular_promedio_internacion(lista_pacientes)

        if promedio_internacion > 0:
            print(f'El promedio de internacion es : {promedio_internacion}')
        else:
            print('No hay promedio que sacar')

    elif opcion_menu == 9:
        print('9')
        Entrar = False
        break
    
        
    input('Apretar para volver al menu principal.....')



