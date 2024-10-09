def buscar_pacientes(lista_pacientes: list[list], historia_clinica: int) -> None:

    no_se_encontro = True

    for i in range(len(lista_pacientes)):

        if lista_pacientes[i][0] == historia_clinica:

            print('*'*30)
            print(f'Historia Clinica: {lista_pacientes[i][0]}')
            print(f'Nombre: {lista_pacientes[i][1]}')
            print(f'Edad: {lista_pacientes[i][2]}')
            print(f'Diagnostico: {lista_pacientes[i][3]}')
            print(f'Cantidad de dias internacion: {lista_pacientes[i][4]}')
            no_se_encontro = False
        
    if no_se_encontro:
        print(f'La historia clinica : {historia_clinica} que busca no se encuentra en el registro')