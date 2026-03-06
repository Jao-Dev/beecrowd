
while True:
    x = int(input());
    if x==0:
        break;
    else:
        n = list(map(int, input().split()));
        maria = n.count(0);
        john = n.count(1);
        print(f"Mary won {maria} times and John won {john} times")
    