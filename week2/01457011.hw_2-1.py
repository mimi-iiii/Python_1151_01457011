import sys
n=int(input())
if n<=1: 
    print("Invalid input")
    sys.exit()
for i in range(n):
    space_count=" "*(n-1-i)
    if i==0:
        print(space_count+"*")
    else:
        middle_space=" "*(2*i-1)
        print(space_count+"*"+middle_space+"*"+space_count)
for i in range(n-2, -1, -1):
    space_count=" "*(n-1-i)
    if i==0:
        print(space_count+"*")
    else:
        middle_space=" "*(2*i-1)
        print(space_count+"*"+middle_space+"*"+space_count)