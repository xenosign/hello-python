# https://school.programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
  strings.sort(key = lambda x: (x[n:n+1], x))
  return strings

ex1 = [["sun", "bed", "car"], 1]
ex2 = [["abce", "abcd", "cdx"], 2]

print(solution(ex1[0], ex1[1]))
print(solution(ex2[0], ex2[1]))