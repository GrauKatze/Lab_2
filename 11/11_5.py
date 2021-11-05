msg = input()
result = len(msg)//2
for i in range(len(msg)):
    if len(msg[i:-i])>0:
        print(msg[i:-i])