x = int(input());
N = list(map(int, input().split()));
menor = min(N);

print(f"Menor valor: {menor}");
print(f"Posicao: {N.index(menor)}");
