n, m= map(int, input().split())
user_input=input()
friendListA=set(map(int, user_input.split()))
user_input=input()
friendListB=set(map(int, user_input.split()))
mutualFriend=sorted(friendListA&friendListB)
print(len(mutualFriend))
if mutualFriend: 
    print(*mutualFriend, sep=" ")