# A = int(input())
# B = [int(x) for x in input().split()]
# C = int(input())
# D = 0
# E = 0
# if B[-1] < 0:
#     D = D + 1
# else:
#     for a in B:
#         if E > C:
#             D = D - 1
#             break
#         else:
#             if a < 0:
#                 E = E+1
#                 continue
#        		D=D+1
#
# print(D,end="")

n = [int(x) for x in input().split(" ")]
s = [int(x) for x in input().split(" ")]
count = 0
for i in range(len(s)):
    l = s[i] - n[1]
    u = s[i]+n[1]
    st = 0
    for x in range(len(s)):
        if not i == x:
            if l <= s[x]<=u:
                st = 1
    count+= 1 if(st == 1) else 0
print(count)
