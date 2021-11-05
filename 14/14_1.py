num = int(input())
rezept = list()
for i in range(num):
    msg = input()
    if 'лук' not in msg:
        rezept.append(msg)
for i in rezept:
    print(i, end=", ")