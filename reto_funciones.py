def enumeracion (numero):
    objetivo= numero
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1

    if respuesta** 2 == objetivo:
        return print(f'La raiz cuadrara de {objetivo} es {respuesta}')
    else:
        return print (f'{objetivo} no tiene una raiz cuadrada exacta')


def aproximacion (numero):
        objetivo = numero
        epsilon = 0.01
        respuesta = 0.0
        paso = epsilon**2
        iteraciones = 0

        while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
            respuesta += paso
            iteraciones += 1

        if abs(respuesta**2 - objetivo) >= epsilon:
            return print(f'No se encontro la raiz cuadrada de {objetivo}')
        else:
            return print(f'La raiz cuadrada de {objetivo} es {respuesta} con {iteraciones} iteraciones')


def b_binaria (numero):
    objetivo = numero
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto+bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo) / 2

    return print(f'La raiz cuadrada de {objetivo} es {respuesta}')


print(f'Bienvenido, este programa va a realizar los calculos de raiz cuadrada, dependiendo la opcion elegida por el usuario y el algoritmo a usar')
objetivo_usr = int(input('Escoge un numero al realizar el calculo de raiz cuadrada: '))

print(f'1: Para enumeración exhaustiva **** 2: Para aproximación de soluciones **** 3: Para búsqueda binaria')
decision = int(input('Escribe tu elección: '))

if decision == 1:
    print(f'Usaste la enumeración exhaustiva: ')
    enumeracion(objetivo_usr)
elif decision == 2:
    print(f'Usaste la aproximación de soluciones: ')
    aproximacion(objetivo_usr)
elif decision == 3:
    print(f'Usaste la búsqueda binaria')
    b_binaria (objetivo_usr)
else:
    print(f'La opcion seleccionada no es valida, vuelva a ejecutar la aplicación')