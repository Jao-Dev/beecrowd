"""Primeira solução"""
"""while True:
    x, y = map(int, input().split());
    if x==0 and y==0:break;
    xN = sorted(set(list(map(int, input().split()))));
    yN = sorted(set(list(map(int, input().split()))));
    trocas=0;

    if len(xN)<len(yN):
        for i in range(len(xN)):
            if xN[i] in yN:
                continue;
            elif yN[i]!=xN[i]:
                trocas+=1;
    else:
        for i in range(len(yN)):
            if yN[i] in xN:
                continue;
            elif xN[i]!=yN[i]:
                trocas+=1;
    print(trocas);"""

while True:
    x, y = map(int, input().split());
    if x==0 and y==0:break;
    xN = set(list(map(int,input().split())));
    yN = set(list(map(int,input().split())));

    trocaX = xN-yN;
    trocaY = yN-xN;

    print(min(len(trocaX), len(trocaY)));