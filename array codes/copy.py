a=[]
n=int(input("enter the number of elements:"))
for i in range (1,n+1):
    a.append(int(input(f"enter the value {i} :")))
print(a)
b=a.copy()
print(f"The copied values {b}")