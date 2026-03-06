x=int(input());

for i in range(x):
    y=int(input())
    z=set(list(map(int,input().split())));
    carneiros=0;
    for i in z:
        carneiros+=1;
    print(carneiros);

