try:
 class factorial:
    def getdata(self):
        self.num=int(input("Enter the Number:"))
    def process(self):
        if self.num<0:
            print(f"cannot find factorial of {self.num}")
        else:
         self.fact=1
         for i in range(1,self.num+1):
             self.fact*=i
             print(self.fact)
             
         
 num=factorial()
 num.getdata()
 num.process()
except Exception as e:
    print(f"invalid option {e}")
finally:
    print("done !")

         
        