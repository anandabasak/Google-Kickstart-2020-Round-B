# cook your dish here
n= int(input())
for _ in range(1,n+1):
    s = input()
    x, y = 0, 0
    mod = 10**9
    stack = []
    moves = ["N", "E","W","S"]
    multiplier = 1
    for c in s:
        if c not in moves:
            if c == ")":
                multiplier //= stack.pop()
            if ord(c) >= ord("2") and ord(c) <= ord("9"):
                multiplier *= int(c)
                stack.append(int(c))
        else:
            if c == "N":
                y -= multiplier
            if c == "S":
                y += multiplier
            if c == "E":
                x += multiplier
            if c == "W":
                x -= multiplier
            x %= mod
            y %= mod
    print("Case #"+str(_)+ ": "+str(x+1)+" "+str(y+1))