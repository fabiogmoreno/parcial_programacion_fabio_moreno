def ingresar_cadenas(mensaje:str,max_caracter:int,max_intento):
    while max_intento != 0:
        cadenas = input(mensaje)
        if cadenas.isalpha():
            if len(cadenas) <= max_caracter:
                return cadenas
            else:
                print(f'Error,como maximo de caracteres es {max_caracter} ')
        else:
            print('Tiene que ingresar solamente letras')
        max_intento -= 1
    return 'superaste el maximo intento y no ingresaste datos'

def ingresar_numeros(mensaje:str,min_rango:int,max_rango:int,max_intento) -> int | str :
    while max_intento != 0: 
        numero = input(mensaje)
        if numero.isdigit():
            if int(numero) >= min_rango and int(numero) <= max_rango:
                return int(numero)
            else:
                print(f'Error,tenes que ingresar entre {min_rango} y {max_rango}')
        else:
            print('Error,solamente tiene que ingresar numeros')
        max_intento -= 1
    print('Nose pudo ingresar numero , ya superaste el maximo intento')

def ingresar_numero_flotante():
    while True:
        entrada = input("Ingresa un número flotante: ")

        # Verificamos si la entrada es válida
        if (entrada.count('.') <= 1 and  # Permitir solo un punto
                ((entrada[0] == '-' and entrada[1:].replace('.', '', 1).isdigit()) or
                 entrada.isdigit() or
                 (entrada[0].isdigit() and entrada[1:].replace('.', '', 1).isdigit()))):
            numero_flotante = float(entrada)
            return numero_flotante
        else:
            print("Entrada inválida. Por favor, ingresa un número flotante que sea válido (ej: 1.5, -2.3).")
