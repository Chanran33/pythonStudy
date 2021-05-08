T = int(input()) #테스트 케이스 갯수

for _ in range(T):
    x = int(input())
    money = [25, 10, 5, 1]
    result = []
    for m in money:
        result.append(x//m)
        x=x%m
    print(*result)#iterator가 되서 하나하나 출력됨.


