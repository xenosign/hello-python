# https://school.programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    answer = 0    

    while (n // 2 != 0) :      
      answer += 1     

      if (abs(a / 2 - b / 2) == 0.5 and max(a, b) % 2 == 0) :
        return answer

      n = n // 2
      a = a // 2 + 1 if a % 2 == 1 else a // 2 
      b = b // 2 + 1 if b % 2 == 1 else b // 2       
    
    return answer

ex1 = [8, 4, 7]
print(solution(ex1[0], ex1[1], ex1[2]))