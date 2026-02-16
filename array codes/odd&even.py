a=int(input("Enter the Range:"))
print()
print("odd numbers:")
odd=[]
for j in range(1,a+1):
    if j%2!=0:
        odd.append(j)
print(odd)
length=len(odd)
print(f"The Count of Odd Numbers :{length}")
print()
print("even numbers:")
even=[]
for i in range(1,a+1):
    if i%2==0:
        even.append(i)
print(even)
length1=len(even)
print(f"The Count of Even Numbers :{length1}")