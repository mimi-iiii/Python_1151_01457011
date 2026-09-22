n= int(input())
for i in range(n):
    s= input()
    char_counts= {}
    for char in s:
        char_counts[char]= char_counts.get(char, 0)+ 1
    most_frequent = max(char_counts, key=char_counts.get)
    print(most_frequent)