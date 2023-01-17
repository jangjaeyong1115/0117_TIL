import sys
input = sys.stdin.readline

Test_case = int(input())

for i in range(Test_case):
    N = int(input())

    print(sum(list(map(int,input().split()))))