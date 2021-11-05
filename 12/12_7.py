N = int(input())
M = int(input())

risunok = list()
for i in range(N):
    risunok.append(input())

for i in range(0,N,2):
    for j in range(0,M,2):
      print(risunok[i][j],end="")
    print()