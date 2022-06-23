# fibonaci

lista = [0,1]
count = 1
while count <= 10:
    lista.append(lista.pop(0) + lista[0])
    print(lista[1])
    count += 1

