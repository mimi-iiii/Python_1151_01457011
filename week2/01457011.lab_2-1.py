count= 1
number= 1
n= int(input());
if n<=0:
    print("Invalid input")
else:
    for i in range(0, n):
        for j in range(0, count):
            print(number, end=" ")
            number= number+ 1
        print()
        count= count+ 1