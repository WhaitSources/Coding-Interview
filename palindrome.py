##
# Write a function solution that, given a string S,
# returns any palindrome which can be obtained by 
# replacing all of the question marks in S by lowercase
# letters ('a'-'z'). If no palindrome can be obtained, 
# the function should return the string "NO".
##

##
# Output :
# ?ab??a : aabbaa
# bab??a : NO
# ?a? : aaa
##

import string

def is_pal(S):
  return S == S[::-1]

def solution(S):
  if '?' in S:
    for c in string.ascii_lowercase:
       S_temp = S.replace("?",c,1)
       res = solution(S_temp)
       if res != "NO":
           return res
  if is_pal(S):
      return S
  else:
      return "NO"

S1 = "?ab??a"
S2 = "bab??a"
S3 = "?a?"
print(S1, " :", solution(S1))
print(S2, " :", solution(S2))
print(S3, " :", solution(S3))
