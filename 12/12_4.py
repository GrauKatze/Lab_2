num = input()
fl_NotEND = True
i = 0
j = 0
for i in range(len(num)):
    if fl_NotEND:
        i = j
        x = num[i]
        count = 0
        j = i
        while x == num[j]:
            count += 1
            if j < len(num)-1:
                j += 1
            else:
                fl_NotEND=False
                break
        print(count, x)
    else:
        break
                    