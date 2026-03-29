a=[]
n=int(input("Enter The Number Of Elements:"))
for i in range (1,n+1):
    a.append(int(input(f"Enter The Value {i} :")))
print(a)
b=a.copy()
print(f"The Copied Values {b}")