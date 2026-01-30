try:
 class temp():
    def getdata(self):
        self.c=int(input("Enter Celsius Tempracture:"))
    def cal(self):
        self.f=(self.c*9/5)+32
    def display(self):
        print(f"The Fahrenhite of {self.c} Celsius is : {self.f}")
 find=temp()
 find.getdata()
 find.cal()
 find.display()
except Exception as e:
    print(f"invalid input {e}")
finally:
    print("done")