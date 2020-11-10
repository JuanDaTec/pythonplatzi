
# Cronometro de una hora, aprendiendo con el profe David y Platzi
# Correra tan rápido como tu PC pueda!

minutos = 0
segundos = 0

while minutos < 60:
    while segundos < 60:
        print(f'{minutos} minutos con {segundos} segundos')
        segundos += 1

    minutos += 1
    segundos = 0

print(f'Se cumplio una hora dentro de nuestro while')


