a=[]
n=int(input("Enter The Element:"))
for j in range(1,n+1):
    a.append(int(input(f"Enter The Number {j}:")))
print()
print(a)
print()
print(f"the largest num is: {max (a)}")
print(f"the smallest num is: {min (a)}")