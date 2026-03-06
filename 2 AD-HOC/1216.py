valores=[];
while True:
    try:
        x=input().strip();
        y=int(input());
        valores.append(y);
    except EOFError:
        break;
print(f"{(sum(valores)/len(valores)):.1f}");