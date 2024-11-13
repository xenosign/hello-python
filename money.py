def solution(price, money, count):
    answer = -1

    totalCharge = 0

    for i in range(1, count + 1) :
        totalCharge += price * i    

    answer = 0 if money - totalCharge >= 0 else totalCharge - money

    return answer

ex1 = [3, 20, 4]

print(solution(ex1[0], ex1[1], ex1[2]))