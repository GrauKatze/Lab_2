num = int(input())*2
spisok = list()
while num>0:
    spisok.append(input())
    num-=1
for i in spisok:
    print(spisok[-i-1],spisok[-i])
    i+=1
