msg = input()
key = list()
j = int()
for i in range(len(msg)):
    if msg[i] == '?':
        for j in range(i+1,len(msg)):
            if msg[j] == '=':
                break
            key.append(msg[j])
        break
for i in range(len(key)):
    print(key[i],end="")
