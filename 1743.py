x=list(map(int,input().split()));
y=list(map(int,input().split()));

if x[0]+y[0]==1 and x[1]+y[1]==1 and x[2]+y[2]==1 and x[3]+y[3]==1 and x[4]+y[4]==1:
    print("Y");
else:print("N");