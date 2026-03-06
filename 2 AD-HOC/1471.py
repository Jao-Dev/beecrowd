while True:
    try:
        x,y=map(int,input().split());

        z=list(map(int,input().split()));
        a=set(range(1, x+1));
        faltam = sorted(set(a)-set(z));

        if not faltam:print("*");
        else:print(*faltam)
    except EOFError:break;