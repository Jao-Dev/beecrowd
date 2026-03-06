while True:
    x = input();
    if x=="*":
        break;
    else:
        iniciais = [palavra[0].lower() for palavra in x.split()];
        todosIguais = len(set(iniciais)) <= 1;
        if todosIguais:
            print("Y");
        else:
            print("N");