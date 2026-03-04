while True:
    x=int(input());
    if x==0:break;

    y=input().strip();
    pos=["N", "L", "S", "O"];
    p=0;
    for i in y:
        if i=="D":p=(p+1)%4;
        else: p=(p-1)%4;
    print(pos[p]);
        