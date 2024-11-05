print("Hello, python")

# 표현식, 몫
print(7 // 3)

# String
a = "This is String"
print(a)

# type
print(type(a))

# 배열로 사용
b = "This is array"
print(b[0])
print(b[-1]) # 역순으로 사용

# 문자열 슬라이싱

## 시작 부터 4 미만까지
c = b[:4]
print(c)

## 4이상 부터 끝가지
d = b[4:]
print(d)

## 간격 2인 문자를 더해서 리턴
f = b[::2]
print(f)

## palindrome 테스트를 할 때 쉽게 하는 법
def isPalindrome(str):
  "Check Palindrome"
  return str == str[::-1]

g = "우영우"
print(isPalindrome(g))
h = "이효석"
print(isPalindrome(h))