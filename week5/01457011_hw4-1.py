def query_system():
    n= int(input().strip())
    students= {}
    for _ in range(n):
        data= input().strip().split()
        if len(data)==3:
            student_id, name, score= data
            students[student_id]= f"{name} {score}"

    q = int(input().strip())

    for _ in range(q):
        query_id = input().strip()
        if query_id in students:
            print(students[query_id])
        else:
            print("Not found")

query_system()