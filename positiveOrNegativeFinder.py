try:
 class pnf():
    def getdata(self):
        self.n=int(input("Enter the number:"))
        
    def process(self):
        if self.n>0:
            print(f"{self.n} is Positive Number")
        elif self.n==0:
            print(f"{self.n} is Zero")
        else:
            print(f"{self.n} is Negetive Number")
            
 find=pnf()
 find.getdata()
 find.process()
except Exception as e:
    print(f"invalid option {e}")
finally:
    print("exit")