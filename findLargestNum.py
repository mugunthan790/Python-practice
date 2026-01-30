class largestnum: 
  def getdata(self):
        self.num1=int(input("Enter the 1st num:"))
        self.num2=int(input("Enter the 2nd num:"))
        self.num3=int(input("Enter the 3rd num:"))
        
  def process(self):
        if self.num1 > self.num2 and self.num1 > self.num3 :
           print(f"{self.num1} is grater then {self.num2} and {self.num3} ")
        elif self.num2 > self.num1 and self.num2 > self.num3 :
           print(f"{self.num2} is grater then {self.num1} and {self.num3} ")
        elif self.num3 > self.num1 and self.num3 > self.num2 :
           print(f"{self.num3} is grater then {self.num1} and {self.num2} ")
num=largestnum()
num.getdata()
num.process()