msg = input()
max = num = int(msg[0:4])
sum = int(msg[4:8])
errors_list = list()

while num > 0:
    msg = input()
    price = int(msg[0:7])
    colum = int(msg[8:12])
    sum -= int(msg[0:7])*int(msg[8:12])
    if (int(msg[0:7])*int(msg[8:12])) != (int(msg[13:17])):
        errors_list.append(max-num+1)
    num -= 1

print(abs(sum))
print(errors_list)