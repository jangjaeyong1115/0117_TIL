N = [] # 리스트 선언

for i in range(9): # 9번 반복
    a = int(input())
    N.append(a)

print(max(N), N.index(max(N))+1, sep = "\n") # max함수로 n의 최댓값 반환, index함수로 max(N)의 위치 반환