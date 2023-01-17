a1, a2 = map(int,input().split())
b1, b2 = map(int,input().split())
c1, c2 = map(int,input().split())

if a1 == b1 :
    d1 = c1

elif a1 == c1 :
    d1 = b1

else : 
    d1 = a1

if a2 == b2:
    d2 = c2

elif a2 == c2:
    d2 = b2

else :
    d2 = a2

print(d1,d2, end=" ")


