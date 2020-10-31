##
# You are given an array of integers. Your task is to create pairs of them, such that
# every pair consists of equal numbers. Each array element may belong to one pair
# only.
##

def solution(A):
    for a1 in range(len(A)):
        for a2 in range(len(A)):
            for b1 in range(len(A)):
                for b2 in range(len(A)):
                    if(A[a1] == A[a2] and A[b1] == A[b2] and a1 != a2 and b1 != b2 and a1 != b1 and a2 != b2 and a1 != b2 and a2 != b1):
                        return True
    return False
