while True:
    h1, m1, h2, m2 = map(int, input().split());
    
    t1 = (h1*60)+m1;
    t2 = (h2*60)+m2;
        
    if t1<t2:
        print((t1-t2)*(-1));
    elif t1>t2:
        tt = (24*60)+t2-t1;
        print(tt);
    elif h1==0 and m1==0 and h2==0 and m2==0:
        break;