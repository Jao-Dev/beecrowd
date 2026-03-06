while True:
    try:
        x = list(map(int, input().split()));
        if sum(x)==1:
            if x[0]==1:
                print("A");
            elif x[1]==1:
                print("B");
            elif x[2]==1:
                print("C");
        elif sum(x)==2:
            if x[0]==0:
                print("A");
            elif x[1]==0:
                print("B");
            elif x[2]==0:
                print("C");
        else:
            print("*");
    except EOFError:
        break;