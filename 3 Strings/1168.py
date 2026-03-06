leds = [2, 5, 5, 4, 5, 6, 3, 7, 6, 6];
x=int(input());

for i in range(x):
    numLeds = 0;
    y=input().strip();
    for i in y:
        numLeds += leds[int(i)-1];
    print(f"{numLeds} leds");