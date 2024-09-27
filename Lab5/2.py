
n = 7

a = [[((i+j)-n+1) for i in range(n)] for j in range(n)]

for r in a:
    print(*r)