def contar_pacientes_5_dias(lista_pacientes: list[list]) -> int:

    contar_paciente = 0

    for i in range(len(lista_pacientes)):
        if lista_pacientes[i][4] > 5:
            contar_paciente += 1
    
    return contar_paciente

def calcular_promedio_internacion(lista_pacientes : list[list]) -> float:

    contador = 0
    acumulador = 0 

    for i in range(len(lista_pacientes)):
        contador += 1
        acumulador += lista_pacientes[i][4]
    
    if contador == 0:
        return 0

    return acumulador / contador