n=int(input());
for i in range(n):
    x=input();

    direita=x[(len(x)//2):];
    esquerda=x[:(len(x)//2)];
    esquerdaR=esquerda[::-1];
    direitaR=direita[::-1];
    print(esquerdaR+direitaR);