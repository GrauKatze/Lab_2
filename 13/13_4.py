status_range_num = int(input())

status_1 = list()
status_2 = list()

for i in range(status_range_num):
    num = int(input())
    status_1.append(num)
    status_2.append(num)

tren_num = int(input())

for i in range(tren_num):
    brat_num = int(input())
    status_num = int(input())
    num = int(input(num))
    if brat_num == 1:
        status_1[status_num] += num
    elif brat_num == 2:
        status_2[status_num] += num

for i in status_1:
    print(i,end=" ")
print()
for i in status_2:
    print(i,end=" ")

num = 0

for i in range(status_range_num):
    if status_1[i] == status_2[i]:
        num += 1

print(num)
