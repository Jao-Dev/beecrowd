while True:
    b, n = map(int, input().split());
    if b==0 and n==0:break;
    reservaBancaria = list(map(int, input().split()));

    for i in range(n):
        d, c, v = map(int, input().split());
        reservaBancaria[d-1]-=v;
        reservaBancaria[c-1]+=v;

    if all(i>=0 for i in reservaBancaria):
        print("S");
    else:print("N");