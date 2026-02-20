a=[]
num=int(input("Enter The Elements:"))
print()
for i in range(1,num+1):
    a.append(int(input(f"Enter The Number {i} :")))
key=int(input("Enter The Search Number:"))
print()
found=False
for j in a:
    if j==key:
      found=True
      break
if found:
    print(f"The Number {key} Is Exists")
else:
    print(f"The Number {key} Is Not Exists")