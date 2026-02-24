x, y, z = map(int, input().split());
lista = [x, y, z];
listaOrdenada = sorted(lista); 

for valor in listaOrdenada:
    print(valor);

print();

for valor in lista:
    print(valor);