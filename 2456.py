x=list(map(int, input().split()));
ordCres=sorted(x);
ordDec=sorted(x, reverse=True);

if x==ordCres:
    print("C");
elif x==ordDec:
    print("D");
else:print("N");