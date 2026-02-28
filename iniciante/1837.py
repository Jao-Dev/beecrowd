x, y = map(int, input().split());

if y<0:
    pos=y*(-1);
    print(f"{(x//pos)*(-1)} {x%pos}");
else:
    print(f"{x//y} {x%y}");