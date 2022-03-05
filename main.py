num=0

num_obtenidos=[]

rango=input('introduzca hasta que numero quiere sumar: ')

while num < int(rango):
    num+=2
    num_obtenidos.append(num)
    

listSum = sum(num_obtenidos)
print(num_obtenidos)
print(f"Suma de los numeros -> {listSum}")
