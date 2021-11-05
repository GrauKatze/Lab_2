num = int(input())
name = list()
kill_name=list()

for i in range(num):
    name.append(input())

kill_num = int(input())

while name:
    for i in range(0,len(name),kill_num-1):
        print(name[i])
        name.remove(name[i])