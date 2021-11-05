msg = input()
num = int(input())
buk = input()
if (num < 1) or (num > len(msg)):
    if len(buk)==1:
        if msg[num] == buk:
            print("YES")
        else:
            print("NO")
    else:
        print("ERROR")
else:
    print("ERROR")