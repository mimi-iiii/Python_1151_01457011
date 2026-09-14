n=int(input())
arr=[int(x) for x in input().split()]
print(*arr)
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1]= arr[j+1], arr[j]
print(*arr)