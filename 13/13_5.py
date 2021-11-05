num = int(input())

comands = list()
comands_point = list()
win_list = list()
not_win_list = list()

not_sort = True

for i in range(num):
    comands.append(input())
    comands_point.append(int(input()))

while not_sort:
    not_sort = False
    for i in range(1,num):
        if comands_point[i-1] < comands_point[i]:
            not_sort = True
            comands_point[i-1], comands_point[i] = comands_point[i], comands_point[i-1]
            comands[i-1], comands[i] = comands[i], comands[i-1]

for i in range(num//2):
    win_list.append(comands[i])
win_list.sort()
for i in win_list:
    print(i)

for i in range(num//2,num):
    not_win_list.append(comands[i])
not_win_list.sort()

for i in not_win_list:
    print(i)
