from timeit import default_timer

objetivo = int(input('Escoge un numero: '))
epsilon = 0.01
respuesta = 0.0
paso = epsilon**2
iteraciones = 0


time_in= default_timer()

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso
    iteraciones += 1

if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada de {objetivo}')
else:
    time_out= default_timer()
    print(f'La raiz cuadrada de {objetivo} es {respuesta} con {iteraciones} iteraciones')
    print('Demorandose ', time_out - time_in , f'segundos en ejecutarse')
