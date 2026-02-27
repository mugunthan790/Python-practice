try:
 a=[]
 e=int(input("Enter The Number Of Elements :"))
 for i in range(1,e+1):
    a.append(int(input(f"Enter The Value {i} :")))
 print(a)
 unique_value=list(set(a))
 print(f"The Output Without  Duplicate Values: {unique_value}")
except Exception as s:
    print(f"Invalid Input {s}")
finally:
    print("DONE")