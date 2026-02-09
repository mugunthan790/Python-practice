a=[]
num=int(input("Enter the elements:"))
print()
for i in range(1,num+1):
    a.append(int(input(f"Enter the number {i} :")))
key=int(input("enter the search number:"))
print()
found=False
for j in a:
    if j==key:
      found=True
      break
if found:
    print(f"The number {key} is exists")
else:
    print(f"the number {key} is not exists")