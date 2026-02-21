try:
 a=[]
 e=int(input("Enter the number of elements :"))
 for i in range(1,e+1):
    a.append(int(input(f"enter the value {i} :")))
 print(a)
 unique_value=list(set(a))
 print(f"the output without  duplicate values: {unique_value}")
except Exception as s:
    print(f"invalid input {s}")
finally:
    print("done")