try:
 class prime:
    def getdata(self):
        self.num=int(input("Enter the number:"))
        
    def process(self):
        if self.num==0 or self.num==1:
            print(f"{self.num} is not a prime number ")
        
        self.count=0
        for i in range(1,self.num+1):
                if(self.num%i==0):
                    self.count+=1
        if self.count ==2:
            print(f"{self.num} is a prime number")
        else:
            print(f"{self.num} is not a prime number")
                    
 num1=prime()
 num1.getdata()
 num1.process()
except Exception as e:
    print(f"invalid option {e}")
finally:
    print("Done")