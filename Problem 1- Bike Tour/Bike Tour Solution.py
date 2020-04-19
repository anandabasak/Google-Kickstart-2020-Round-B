n = int(input())
for _ in range(1,n+1):
    l = int(input())
    count = 0
    arr = list(map(int, input().split()))
    for i in range(1,l-1):
        if(arr[i-1]<arr[i]>arr[i+1]):
            count+=1
    print("Case #"+str(_)+": "+ str(count))
    
