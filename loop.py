def print_separator(message):
    """구분선을 출력하는 헬퍼 함수"""
    print("\n" + "=" * 50)
    print(f"예제: {message}")
    print("=" * 50)

def example_basic_for():
    print_separator("기본 for 반복문")
    
    print("1. 리스트 순회:")
    fruits = ["사과", "바나나", "오렌지"]
    for fruit in fruits:
        print(fruit)
    
    print("\n2. range() 사용:")
    for i in range(5):
        print(i, end=" ")  # 0부터 4까지
    print()

def example_while():
    print_separator("while 반복문")
    
    count = 0
    while count < 5:
        print(count, end=" ")
        count += 1
    print()

def example_nested_loop():
    print_separator("중첩 반복문 (구구단 2~3단)")
    
    for i in range(2, 4):  # 예제를 위해 2~3단만 출력
        print(f"\n{i}단:")
        for j in range(1, 10):
            print(f"{i} x {j} = {i*j}")

def example_break_continue():
    print_separator("break와 continue")
    
    print("break 예제 (5에서 중단):")
    for i in range(10):
        if i == 5:
            break
        print(i, end=" ")
    print()
    
    print("\ncontinue 예제 (2를 건너뜀):")
    for i in range(5):
        if i == 2:
            continue
        print(i, end=" ")
    print()

def example_loop_else():
    print_separator("else와 함께 사용하는 반복문")
    
    # 정상적으로 완료되는 경우
    print("1. 정상 완료:")
    for i in range(3):
        print(i, end=" ")
    else:
        print("\n반복문이 정상적으로 완료되었습니다!")
    
    # break로 중단되는 경우
    print("\n2. break로 중단:")
    for i in range(3):
        if i == 2:
            print("\nbreak 발생!")
            break
        print(i, end=" ")
    else:
        print("이 메시지는 출력되지 않습니다.")

def main():
    print("파이썬 반복문 예제 모음")
    example_basic_for()
    example_while()
    example_nested_loop()
    example_break_continue()
    example_loop_else()

if __name__ == "__main__":
    main()