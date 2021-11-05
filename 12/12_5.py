res = str(1/int(input()))
word = res[2:]

for j in range(len(word)):
    for i in range(j+1,len(word)):
        if word[j:i]==word[i:i+i-j]:
            print(word[j:i])
            exit()
print(0)