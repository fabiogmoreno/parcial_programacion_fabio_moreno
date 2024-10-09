 
from validacion import ingresar_cadenas,ingresar_numeros
 
 
def cargar_pacientes(lista_paciente: list[list],cantidad_pacientes: int) -> list[list] : 

    

    while cantidad_pacientes != 0:

        historia_clinica = ingresar_numeros('Ingrese el numero de historia clinicia: ',1,5000,5)
        nombre_paciente = ingresar_cadenas('Ingrese el nombre del paciente : ',10,5)
        edad_paciente = ingresar_numeros('Ingrese la edad del paciente ',1,100,5)
        diagnostico = ingresar_cadenas('Ingrese el diagnostico por favor: ',15,5)
        cantidad_dias_internacion = ingresar_numeros('Ingrese la cantidad de dias de internacion: ',1,100,5)

        lista_agregar = [historia_clinica,nombre_paciente,edad_paciente,diagnostico,cantidad_dias_internacion]

        lista_paciente += [lista_agregar]

        cantidad_pacientes -= 1
    
    return lista_paciente

 