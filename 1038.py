x, y = map(int, input().split());

if x==1:
    total = y*4;
    print(f"Total: R$ {total:.2f}");
elif x==2:
    total = y*4.5;
    print(f"Total: R$ {total:.2f}");
elif x==3:
    total = y*5;
    print(f"Total: R$ {total:.2f}");
elif x==4:
    total = y*2;
    print(f"Total: R$ {total:.2f}");
elif x==5:
    total = y*1.5;
    print(f"Total: R$ {total:.2f}");