a=[]
n=int(input("Enter The Element:"))
for j in range(1,n+1):
    a.append(int(input(f"Enter The Number {j}:")))
print()
print(a)
print()
print(f"The Largest Number Is: {max (a)}")
print(f"The Smallest Number Is: {min (a)}")