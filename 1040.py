x, y, z, a = map(float, input().split());

pX = 2*x;
pY = 3*y;
pZ = 4*z;
pA = 1*a;

media = (pX+pY+pZ+pA)/10;

print(f"Media: {media:.1f}");

if media>=7:
    print("Aluno aprovado.");
elif media<5:
    print("Aluno reprovado.");
elif media>=5 and media<=6.9:
    print("Aluno em exame.");
    nE = float(input());
    mF = (nE+media)/2;
    print(f"Nota do exame: {nE:.1f}");
    if mF>=5:
        print("Aluno aprovado.");
        print(f"Media final: {mF:.1f}")
    else:
        print("Aluno reprovado.");
        print(f"Media final: {mF:.1f}")
