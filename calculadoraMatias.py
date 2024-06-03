import logging

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def operacion (operador, a, b):
    try:
        if operador == "+":
            return sumar(a, b)
        elif operador == "-":
            return restar(a, b) 
        elif operador == "x":
            return multiplicar(a, b)
        elif operador == "/":
            return dividir(a, b)
    except ZeroDivisionError as err1:
        print ('No se puede dividir en 0. Intente otra operación.')
        registrarError('Error de division', err1)
    except OverflowError as err2:
        print ('Los valores que ingresó son demasiado grandes. Intente otra operación.')
        registrarError('Error de overflow', err2)
    except Exception as err3:
        print ('Ocurrió un error inesperado. Intente otra operación.')
        registrarError('Error inesperado', err3)

def registrarError(mensaje, error):
    logging.basicConfig(filename='errores.log', level=logging.ERROR)
    logging.error(f"{mensaje}: {error}")

def esOperador(caracter):
    if caracter != "+" and caracter != "-" and caracter != "x" and caracter != "/":
        return False
    else:
        return True
    
def obtenerNumero():
    while True:
        try: 
            num = input("Ingrese un numero: ")
            if num.upper() == "S": #upper convierte el valor de -num- en mayuscula
                return 
            else:
                num = float(num)
            return num
        except ValueError as err4:    
            registrarError('Error de Valor Incorrecto', err4)
            print ("Eso no es numero. Intente de nuevo.")

def obtenerOperador():
    while True:
        operador = input("\nSuma --> +\nResta --> -\nMultiplicación --> x\nDivisión --> /\n\nIngresa un operador: " )

        if operador.upper() == "S":
            return 
        elif not esOperador(operador):
            print("Error. Eso no es un operador válido")
        else:
            return operador


def calculadora():
    print("Bienvenido a la calculadora!")
    print("Cuando desee salir, puede ingresar la tecla S")
    salir = False
    while salir == False:
        
        a = obtenerNumero()
        if a == None: 
            salir = True
            continue

        operador = obtenerOperador()
        if operador == None:
            salir = True
            continue

        b = obtenerNumero()
        if b == None:
            salir = True
            continue

        resultado = operacion(operador, a, b)
        if resultado != None:
            print ("El resultado es: " + str(resultado))
    
    print("Saliste de la calculadora!")

calculadora()
