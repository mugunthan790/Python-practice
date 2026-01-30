try:
 class LargestNumber:
    def getdata(self):
        self.num1=int(input("enter 1st number:"))
        self.num2=int(input("Enter 2nd number:"))
        self.num3=int(input("Enter 3rd number:"))
        
    def process(self):
        if self.num1>self.num2 and self.num3:
            print(f"{self.num1} is greater then {self.num2} and {self.num3}")
        elif self.num2>self.num3 and self.num1:
            print(f"{self.num2} is greater then {self.num1} and {self.num3}")
        elif self.num3>self.num1 and self.num2:
            print(f"{self.num3} is greater then {self.num1} and {self.num2}")
            
 num=LargestNumber()
 num.getdata()
 num.process()
except Exception as e:
    print("invalid",e)
finally:
    print("done")