a = ['a', 'b', 'c']

# 리스트로 추가
a.append('d')
print(a)  # ['a', 'b', 'c', 'd']

# 리스트 확장
a.extend(['e', 'f']) 
print(a)  # ['a', 'b', 'c', 'd', 'e', 'f']

# 특정 위치에 삽입
a.insert(1, 'x')
print(a)  # ['a', 'x', 'b', 'c', 'd', 'e', 'f']

# 제거
a.remove('x')
print(a)  # ['a', 'b', 'c', 'd', 'e', 'f']

# 마지막 요소 제거 및 반환
popped = a.pop()  
print(popped)  # 'f'
print(a)  # ['a', 'b', 'c', 'd', 'e']

# 특정 인덱스 제거 후 반환
popped_index = a.pop(1)
print(popped_index)  # 'b'
print(a)  # ['a', 'c', 'd', 'e']

# 요소의 인덱스 찾기
index = a.index('c')  
print(index)  # 1

# 특정 요소의 개수 세기
count = a.count('a')
print(count)  # 1

# 리스트 뒤집기
a.reverse()
print(a)  # ['e', 'd', 'c', 'a']

# 오름차순 정렬
a.sort()
print(a)  # ['a', 'c', 'd', 'e']

# 내림차순 정렬
a.sort(reverse=True)  
print(a)  # ['e', 'd', 'c', 'a']

# 모든 요소 제거
a.clear()  
print(a)  # []

# 리스트 복사
b = ['a', 'b', 'c']
c = b.copy()  # 리스트 복사
print(c)  # ['a', 'b', 'c']