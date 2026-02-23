x = float(input());

print("NOTAS:")
for nota in [100, 50, 20, 10, 5, 2]:
    qtd = x//nota;
    print(f"{qtd:.0f} nota(s) de R$ {nota:.2f}");
    x %= nota;
print("MOEDAS:")
for moeda in [1, 0.50, 0.25, 0.10, 0.05, 0.01]:
    qtd = x//moeda;
    print(f"{qtd:.0f} moeda(s) de R$ {moeda:.2f}");
    x %= moeda;
