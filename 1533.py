while True:
    x=int(input());
    if x==0:break;
    y=list(map(int,input().split()));
    maiorSus=y[0];
    z=0;
    for i in range(len(y)):
        if(maiorSus==max(y)):
            z=0;
        else:z=y.index(max(y));
    for i in range(len(y)):
        if(i==z):
            y[i]=0;
    sus=y.index(max(y))+1;
    print(sus)

