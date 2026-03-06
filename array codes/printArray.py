a=[]
n=int(input("Enter The Elements:"))
for i in range(1,n+1):
    a.append(int(input(f"Enter The Number {i} :")))
print(a)
rev=a[::-1]
print(f"The Reversed String is {rev}")