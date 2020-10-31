##
# There are N coins, each showing either heads or tails. We would like all the coins to
# form a sequence of alternating heads and tails. What is the minimum number of
# coins that must be reversed to acheive this ?
##

##
# Output :
# [1, 0, 1, 0, 1, 1]  : 1
# [1, 1, 0, 1, 1]     : 2
# [0, 1, 0]           : 0
# [0, 1, 1, 0]        : 2
##
def solution(A):
    s1 = 0
    s2 = 0
    for i, n in enumerate(A):
        s1 = s1 + (n == (i % 2))
        s2 = s2 + (n == ((i + 1) % 2))

    return min(s1, s2)    

A1 = [1,0,1,0,1,1]
A2 = [1,1,0,1,1]
A3 = [0,1,0]
A4 = [0,1,1,0]

print(A1, ":",solution(A1))
print(A2, ":",solution(A2))
print(A3, ":",solution(A3))
print(A4, ":",solution(A4))
