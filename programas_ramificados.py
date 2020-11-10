print('Bienvenido, este programa va a comparar las edades de dos usuarios')
nom_usr1= input(f'Escriba el nombre del primer usuario: ')
edad_usr1 = int(input(f'Digite la edad que tiene {nom_usr1}: '))
nom_usr2= input(f'Escriba el nombre del segundo usuario: ')
edad_usr2 = int(input(f'Digite la edad que tiene {nom_usr2}: '))

if edad_usr1 > edad_usr2:
    print (f'El usuario {nom_usr1} es mayor que {nom_usr2}')
elif edad_usr1 < edad_usr2:
    print (f'El usuario {nom_usr1} es menor que {nom_usr2}')
else:
    print (f'Los dos usuarios tienen la misma edad')