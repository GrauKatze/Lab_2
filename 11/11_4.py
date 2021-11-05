num = int(input())
code = list()
resultat = list()
i = 0

while i != num:
    code.append(input())
    i+=1

for word in code:
    resultat.append(word.split())
    