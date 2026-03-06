x = int(input());

for i in range(x):
    y = input();
    d1 = int(y[0]);
    d2 = int(y[2]);

    if y[0]==y[2]:
        print(d1*d2);
    elif y[1].isupper():
        print(d2-d1);
    else:
        print(d1+d2);