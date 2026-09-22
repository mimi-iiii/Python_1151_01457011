n, d_sq= map(int, input().split())

sensors= set()
for i in range(n):
    x, y, z, p= map(int, input().split())
    sensors.add((x, y, z, p))

interference_pairs = set()

for i in sensors:
    for j in sensors:
        if i== j:
            continue

        dist_sq= (i[0]-j[0])**2+(i[1]-j[1])**2+(i[2]-j[2])**2
        if dist_sq<=d_sq and i[3]!=j[3]:
            if i<j:
                pair= (i, j)
            else:
                pair= (j, i)
            interference_pairs.add(pair)

sorted_pairs= sorted(list(interference_pairs))

print(f"Interference Pairs: {len(sorted_pairs)}")
for pair in sorted_pairs:
    i, j= pair
    print(f"({i[0]}, {i[1]}, {i[2]}, {i[3]}) <-> ({j[0]}, {j[1]}, {j[2]}, {j[3]})")