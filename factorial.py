
class factorial:
    def getdata(self):
        self.num=int(input("Enter the number:"))
    def process(self):
        if self.num<0:
            print(f"cannot find factorial of {self.num}")
        else:
         self.fact=1
         for i in range(1,self.num+1):
             self.fact*=i
             print(self.fact)
             
         
num1=factorial()
num1.getdata()
num1.process()

         
        