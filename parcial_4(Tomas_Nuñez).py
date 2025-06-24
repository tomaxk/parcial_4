registro={}

def validar_nombre(nombre):
    if nombre in registro:
        print('El nombre ya se encuentra registrado')
    elif len(nombre)==0:
        print('por favor ingrese un nombre')
    else:
        print('El nombre fue registrado exitosaente')
        return True

def validar_entrada(entrada):
    if entrada=='G':
        print('Entrada registrada como "General"')
        return True
    elif entrada=='V':
        print('Entrada registrada como "VIP"')
        return True
    else:
        print('Debe ingresar un tipo de entrada valido')

def validar_codigo(codigo):
    letras=0
    numero=0
    vacio=0
    for caracter in codigo:
        if caracter.isupper():
            letras+=1
        elif caracter.isdigit():
            numero+=1
        elif caracter.isspace():
            vacio+=1
    
    if len(codigo)<6:
        print('Codigo no valido, intente otra vez')
    elif vacio>0:
        print('ERROR, el codigo de confirmacion no puede contener espacios en blanco')
    elif letras<1:
        print('ERROR, el codigo debe contener al menos 1 letra mayuscula')
    elif numero<1:
        print('ERROR, el codigo debe contener al menos 1 numero')
    else:
        return True


    

def registrar_comprador():
    while True:
        nombre=input('Ingrese el nombre del comprador: ')
        if validar_nombre(nombre)==True:
            break

    while True:
        entrada=input('Ingrese el tipo de entrada que desea comprar (G/V): ')
        if validar_entrada(entrada)==True:
            break

    while True:
        codigo=input('Ingrese el codigo de confirmacion: ')
        if validar_codigo(codigo)==True:
            print('El codigo fue regstrado con exito')
            break

    registro[nombre]={
        'entrada':entrada,
        'codigo':codigo
    }
    print('El comprador fue registrado con exito')
        
def buscar_comprador():
    nombre=input('Ingrese el nombre del comprador que desea consultar: ')
    encontrado=False
    for clave, valor in registro.items():
        if clave==nombre:
            print(f'Nombre: {clave} - Tipo de entrada: {valor['entrada']} - Codigo de confiracion: {valor['codigo']}')
            encontrado=True
    if encontrado==False:
        print('El coprador no se encuentra')

def cancelar_compra(nombre):
    if nombre in registro:
        del registro[nombre]
        print('Compra cancelada!!')
    else:
        print('El comprador no se encuentra')


while True:
    print('-----MENU CONCIERTO-----')
    print('1.- Comprar entrada')
    print('2.- Consultar comprador')
    print('3.- Cancelar compra')
    print('4.- Salir')
    opcion=input('Ingrese opcion: ')

    match opcion:
        case '1':
            registrar_comprador()
        case '2':
            if len(registro)==0:
                print('No se han ingresado compradores al sistema')
            else:
                buscar_comprador()
        case '3':
            if len(registro)==0:
                print('No se han ingresado compradores al sistema')
            else:
                nombre=input('Ingrese el nombre del comprador a cancelar: ')
                cancelar_compra(nombre)
        case '4':
            print('Saliendo del sistema...')
            break
        case default:
            print('Debe ingresar una opción válida!!')