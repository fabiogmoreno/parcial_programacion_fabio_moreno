
def mostrar_pacientes(lista_pacientes: list[list]):

    for i in range(len(lista_pacientes)):
        print('*'*20)
        print(f'Historia Clinica: {lista_pacientes[i][0]}')
        print(f'Nombre: {lista_pacientes[i][1]}')
        print(f'Edad: {lista_pacientes[i][2]}')
        print(f'Diagnostico: {lista_pacientes[i][3]}')
        print(f'Cantidad de dias internacion: {lista_pacientes[i][4]}')

def producto_mas_caro(lista:list[list])->None:

    max_precio = float('-inf')
    
    for i in range(len(lista)):

        if lista[i][1] > max_precio:
            max_precio = lista[i][1]
    
    print(f'El mas caro de los producto es con el precio: {max_precio} ')

def mostrar_maximo_internacion(lista_pacientes: list[list]):

    max_internacion = float('-inf')

    for i in range(len(lista_pacientes)):

        if lista_pacientes[i][4] > max_internacion:
            max_internacion =  lista_pacientes[i][4]
            index_max = i

    if (len(lista_pacientes) > 0):
        print('El paciente con mas dias de internacion:  ')
        print('*'*20)
        print(f'Historia Clinica: {lista_pacientes[index_max][0]}')
        print(f'Nombre: {lista_pacientes[index_max][1]}')
        print(f'Edad: {lista_pacientes[index_max][2]}')
        print(f'Diagnostico: {lista_pacientes[index_max][3]}')
        print(f'Cantidad de dias internacion: {lista_pacientes[index_max][4]}')
        print(max_internacion)
    else:
        print('No hay pacientes que mostrar')
    
def mostrar_minimo_internacion(lista_pacientes: list[list]):

    min_internacion = float('inf')

    for i in range(len(lista_pacientes)):

        if lista_pacientes[i][4] < min_internacion:
            min_internacion =  lista_pacientes[i][4]
            index_min = i

    if (len(lista_pacientes) > 0):
        print('El paciente con menos dias de internacion:  ')
        print('*'*20)
        print(f'Historia Clinica: {lista_pacientes[index_min][0]}')
        print(f'Nombre: {lista_pacientes[index_min][1]}')
        print(f'Edad: {lista_pacientes[index_min][2]}')
        print(f'Diagnostico: {lista_pacientes[index_min][3]}')
        print(f'Cantidad de dias internacion: {lista_pacientes[index_min][4]}')
    else: 
        print('No hay paciente que mostrar')