
def generateprimenumbers(upper):
    pnlist = []
    for num in range(0, upper + 1):
       # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                pnlist.append(num)
    return pnlist


def checknumber(num):
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


A, B = input().split(" ")
C = int(A)//int(B)
plist = generateprimenumbers(C)
# print(C)
# print(plist)
final = 0

for pl in plist:
    D = pl
    Q = 0
    for E in range(int(B)-1):
        D = D + C
        F = checknumber(D)
        # print(D,end=" ")
        if not F:
            Q = 1
            break
    if Q == 0:
        final = final + 1
    # print()

print(final)

# print(checknumber(11))



