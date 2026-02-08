a=[]
n=int(input("enter the element:"))
for j in range(1,n+1):
    a.append(int(input(f"Enter the number {j}:")))
print()
print(a)
print()
print(f"the largest num is: {max (a)}")
print(f"the smallest num is: {min (a)}")