x,y=map(int,input().split());
alunos=[];
for i in range(x):
    alunos.append(input().strip());
alunos.sort();
print(alunos[y-1]);
