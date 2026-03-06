"""Cifra de César"""

N=int(input());
for i in range(N):
    alfabeto = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ");

    y=input().strip();
    x=int(input());
    z=[];

    for i in y:
        a=alfabeto.index(i);
        b=z.index(i) if i in z else len(z);
        z.append(alfabeto[(a-x)%26]);

    print("".join(z));