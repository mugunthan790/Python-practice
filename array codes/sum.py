a=[]
for i in range(1,6):
    a.append(int(input(f"Enter The Number {i}:")))
print(a)
total=0
for j in a:
    total+=j
print(f"The sum of all numbres : {total}")