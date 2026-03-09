"""while True:
    try:
        x=input()
        resultado=""

        for i in range(0, len(x)):
            if i%2==0:resultado+=x[i].upper()
            else:resultado+=x[i].lower()

        print(resultado)
    except EOFError:break"""

while True:
    try:
        x = input()
        resultado = ""
        upper = True

        for c in x:
            if c.isalpha():
                if upper:
                    resultado += c.upper()
                else:
                    resultado += c.lower()
                upper = not upper
            else:
                resultado += c

        print(resultado)
    except EOFError:
        break
