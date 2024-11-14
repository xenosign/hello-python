def solution(s):
    answer = s.isdigit() and (len(s) == 4 or len(s) == 6)    
    return answer

ex1 = "a234"
ex2 = "1234"

print(solution(ex1))
print(solution(ex2))