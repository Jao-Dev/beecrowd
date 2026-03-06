while True:
    x = int(input())
    if x==0:
        break;
    else:
        yM = 0;
        zM = 0;
        for i in range(x):
            y, z = map(int, input().split());
            if y>z:
                yM+=1;
            elif y<z:
                zM+=1;
        print(yM, zM);

