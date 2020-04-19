n = int(input())
for _ in range(1,n+1):
    t , d = map(int, input().split())
    arr = list(map(int, input().split()))
    reach = d
    for i in reversed(range(t)):
        reach = ((reach)//arr[i])*arr[i]
    print("Case #"+str(_)+": "+ str(reach))