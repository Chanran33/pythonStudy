N = int(input()) #토핑 종류의 수
A, B = map(int,input().split()) #도우의 가격A, 토핑의 가격 B
C = int(input()) #도우의 열량
 
D = [] #토핑의 열량들
for _ in range(N):
    x=int(input())
    D.append(x)

# D = []
for i in range(1,N+1):
    price = A + B*i #토핑 선택 갯수에 따라서 가격 달라짐
