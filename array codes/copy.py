a=[]
n=int(input("Enter The Number of Elements:"))
for i in range (1,n+1):
    a.append(int(input(f"enter the value {i} :")))
print(a)
b=a.copy()
print(f"The copied values {b}")