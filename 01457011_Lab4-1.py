def carryCheck(x, y):
    carryCount= 0
    currentCarry= 0
    
    maxlen= max(len(x), len(y))
    n1=x.zfill(maxlen)[::-1]
    n2=y.zfill(maxlen)[::-1]
    
    for i in range (maxlen):
        check=int(n1[i])+int(n2[i])+currentCarry
        if check>=10: 
            carryCount+=1
            currentCarry= check/10
        else:
            currentCarry=0
    return carryCount
while True:
    try:
        line= input().strip()
        parts=line.split()
        n1=parts[0]
        n2=parts[1]
        if (n1=='0' and n2=='0'): break
        carries= carryCheck(n1, n2)
        if carries==0:
            print("No carry operation.")
        elif carries==1:
            print("1 carry operation.")
        else:
            print(f"{carries} carry operations.")
    except EOFError:
        break