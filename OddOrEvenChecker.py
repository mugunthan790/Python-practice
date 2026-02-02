class oe:
    def getdata(self):
        self.num=int(input("Enter the Number:"))
        
    def process(self):
        if self.num%2==0:
            print(f"{self.num} is Even Number")
        else:
            print(f"{self.num} is Odd Number")
            
num1=oe()
num1.getdata()
num1.process()