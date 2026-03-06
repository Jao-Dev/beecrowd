while True:
    x,y=input().split();
    if x=="0" and y=="0":break;

    z=y.replace(x, '')
    if not z:print(0);
    else:print(int(z));