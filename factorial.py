try:
 class factorial:
    def getdata(self):
        self.n=int(input("Enter the number:"))
    def process(self):
        if self.n<0:
            print(f"cannot find factorial of {self.n}")
        else:
         self.f=1
         for i in range(1,self.n+1):
             self.f*=i
             print(self.f)
             
         
 num=factorial()
 num.getdata()
 num.process()
except Exception as e:
    print(f"invalid option {e}")
finally:
    print("done")

         
        