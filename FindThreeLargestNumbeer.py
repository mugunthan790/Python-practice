try:
 class LargestNumber:
    def getdata(self):
        self.n1=int(input("Enter 1st number:"))
        self.n2=int(input("Enter 2nd number:"))
        self.n3=int(input("Enter 3rd number:"))
        
    def process(self):
        if self.n1>self.n2 and self.n3:
            print(f"{self.n1} is greater then {self.n2} and {self.n3}")
        elif self.n2>self.n3 and self.n1:
            print(f"{self.n2} is greater then {self.n1} and {self.n3}")
        elif self.n3>self.n1 and self.n2:
            print(f"{self.n3} is greater then {self.n1} and {self.n2}")
            
 num=LargestNumber()
 num.getdata()
 num.process()
except Exception as e:
    print("invalid",e)
finally:
    print("done")