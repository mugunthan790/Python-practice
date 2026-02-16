a=[]
n=int(input("Enter The Element:"))
for j in range(1,n+1):
    a.append(int(input(f"Enter The Number {j}:")))
print()
print(a)
print()
print(f"the Largest number is: {max (a)}")
print(f"the Smallest number is: {min (a)}")