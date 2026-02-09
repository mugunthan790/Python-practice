a=[]
n=int(input("enter the elements:"))
for i in range(1,n+1):
    a.append(int(input(f"Enter the number {i} :")))
print(a)
rev=a[::-1]
print(f"The reversed string is {rev}")