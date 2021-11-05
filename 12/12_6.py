msg = input().upper()
A = ['  *  ',
     ' * * ',
     '*   *',
     '*****',
     '*   *']

B = ['**** ',
     '*   *',
     '*****',
     '*   *',
     '**** ']

C = [' *** ',
     '*   *',
     '*    ',
     '*   *',
     ' *** ']

D = ['**** ',
     '*   *',
     '*   *',
     '*   *',
     '**** ']

E = ['*****',
     '*    ',
     '***  ',
     '*    ',
     '*****']

F = ['*****',
     '*    ',
     '***  ',
     '*    ',
     '*    ']

G = ['*****',
     '*    ',
     '*  **',
     '*   *',
     '*****']

H = ['*   *',
     '*   *',
     '*****',
     '*   *',
     '*   *']

I = ['*****',
     '  *  ',
     '  *  ',
     '  *  ',
     '*****']

J = ['*****',
     '   * ',
     '   * ',
     '   * ',
     '***  ']

K = ['*   *',
     '*  * ',
     '***  ',
     '*  * ',
     '*   *']

L = ['*    ',
     '*    ',
     '*    ',
     '*    ',
     '*****']

M = [' * * ',
     '* * *',
     '*   *',
     '*   *',
     '*   *']

N = ['*   *',
     '*  **',
     '* * *',
     '**  *',
     '*   *']

O = [' *** ',
     '*   *',
     '*   *',
     '*   *',
     ' *** ']

P = ['*****',
     '*   *',
     '*****',
     '*    ',
     '*    ']

Q = [' **  ',
     '*  * ',
     '*  * ',
     '*  * ',
     ' ****']

R = ['**** ',
     '*   *',
     '**** ',
     '*  * ',
     '*   *']

S = [' ****',
     '*    ',
     ' *** ',
     '    *',
     '**** ']

T = ['*****',
     '  *  ',
     '  *  ',
     '  *  ',
     '  *  ']

U = ['*   *',
     '*   *',
     '*   *',
     '*   *',
     ' *** ']

V = ['*   *',
     '*   *',
     '*   *',
     ' * * ',
     '  *  ']

W = ['*   *',
     '*   *',
     '*   *',
     '* * *',
     ' * * ']

X = ['*   *',
     ' * * ',
     '  *  ',
     ' * * ',
     '*   *']

Y = ['*   *',
     '*   *',
     '  *  ',
     '  *  ',
     '  *  ']

Z = ['*****',
     '    *',
     '  *  ',
     '*    ',
     '*****']

print_msg = list()

for i in msg:
    if i == 'A':
        print_msg.append(A)
    elif i == 'B':
        print_msg.append(B)
    elif i == 'C':
        print_msg.append(C)
    elif i == 'D':
        print_msg.append(D)
    elif i == 'E':
        print_msg.append(E)
    elif i == 'F':
        print_msg.append(F)
    elif i == 'G':
        print_msg.append(G)
    elif i == 'H':
        print_msg.append(H)
    elif i == 'I':
        print_msg.append(I)
    elif i == 'J':
        print_msg.append(J)
    elif i == 'K':
        print_msg.append(K)
    elif i == 'L':
        print_msg.append(L)
    elif i == 'M':
        print_msg.append(M)
    elif i == 'N':
        print_msg.append(N)
    elif i == 'O':
        print_msg.append(O)
    elif i == 'P':
        print_msg.append(P)
    elif i == 'Q':
        print_msg.append(Q)
    elif i == 'R':
        print_msg.append(R)
    elif i == 'S':
        print_msg.append(S)
    elif i == 'T':
        print_msg.append(T)
    elif i == 'U':
        print_msg.append(U)
    elif i == 'V':
        print_msg.append(V)
    elif i == 'W':
        print_msg.append(W)
    elif i == 'X':
        print_msg.append(X)
    elif i == 'Y':
        print_msg.append(Y)
    elif i == 'Z':
        print_msg.append(Z)

for j in range(5):
    for i in print_msg:
        print(i[j], "  ", end="")
    print()
