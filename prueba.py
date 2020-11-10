i = 0
pos = 0
neg = 0
pares = 0
impares = 0
mult_4 = 0
mult_5 = 0

lista = []
iterador = 5

for i in range(iterador):
    print('Ingresa el valor del numero en la posicion' ,  i+1)
    valor = int(input(''))
    lista.append(valor)
print(lista)
for i in range(iterador):
    if lista[i] > 0:
        pos = pos + 1
    elif lista[i] < 0:
        neg = neg + 1
    
    
    if lista[i] % 2 == 0:
        pares = pares +1
        
print("negativos" , neg , "positivos" , pos , "pares" , pares)