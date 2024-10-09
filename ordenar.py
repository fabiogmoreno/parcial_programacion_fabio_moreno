def ordenar_pacientes(lista_paciente: list[list]) -> list:

    for i in range(len(lista_paciente)):
        for j in range(len(lista_paciente)-1-i):
            if lista_paciente[j][0] > lista_paciente[j+1][0]:
                aux = lista_paciente[j+1]
                lista_paciente[j+1] = lista_paciente[j]
                lista_paciente[j] = aux
    
    return lista_paciente