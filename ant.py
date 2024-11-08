def solution(hp):
  answer = 0

  while hp > 0:
    print(answer)
    if hp >= 5: 
      answer += hp // 5
      hp = hp % 5
    elif hp >= 3:
      answer += hp // 3
      hp = hp % 3
    else :
      answer += hp // 1
      hp = hp % 1

  return answer

ex1 = 23
ex2 = 999

print(solution(ex1))
print(solution(ex2))

# 다른 사람 풀이
def solution(hp):    
  return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)