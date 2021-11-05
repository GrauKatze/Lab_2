num = int(input())
white_list = list()
block_list = list()

while num > 0:
    white_list.append(input())
    num -= 1

num = int(input())

while num > 0:
    block_list.append(input())
    num -= 1

for word in block_list:
    if word in white_list:
        print(word)