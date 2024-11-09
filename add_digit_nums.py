def solution(n):
    answer = 0

    strNum = str(n)

    for digit in strNum:
        answer += int(digit)    

    return answer

ex1 = 123
ex2 = 987

print(solution(ex2))