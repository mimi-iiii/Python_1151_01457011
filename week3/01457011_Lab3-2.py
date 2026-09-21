import sys
n=int(input())
while True:
    num=input()
    if num.strip()=="0":
        sys.exit()
    train=list(map(int, num.split()))
    stack=[]
    current=1
    possible=True
    for t in train:
        while not stack or stack[-1]!=t:
            if current>n:
                possible=False
                break
            stack.append(current)
            current+=1
        if possible and stack[-1]==t:
            stack.pop()
        else:
            possible=False
            break
    if possible:
        print("YES")
    else:
        print("NO")