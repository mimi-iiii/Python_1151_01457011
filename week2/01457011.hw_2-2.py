import sys
tokens=sys.stdin.read().split()
arr=[]
for t in tokens:
    inserted= False
    for i in range(len(arr)):
        if int(t)<arr[i]:
            arr.insert(i, int(t))
            inserted= True
            break
    if not inserted:
        arr.append(int(t))
    n=len(arr)
    if n%2==0:
        middle=(arr[n//2]+arr[n//2-1])//2
    else:
        middle=arr[n//2]
    print(middle)