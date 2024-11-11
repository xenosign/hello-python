def solution(s):
    answer = ''

    strLen = len(s)
    midIdx = strLen // 2

    if (strLen % 2 == 0) :      
      answer = s[midIdx - 1:midIdx + 1]      
    else :
      answer = s[midIdx:midIdx + 1]
    
    return answer

ex1 = "abcde"
ex2 = "qwer"

print(solution(ex1))
print(solution(ex2))

