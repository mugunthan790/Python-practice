try:
 class count():
    def getdata(self):
       self.num=int(input("Enter the Number:"))
    def process(self):
        self.count=0
        for self.i in range(1,self.num+1):
         if self.i%2==0:
          print(self.i)
          self.count=self.count+1
        print(f"count={self.count}")
 count1=count()
 count1.getdata()
 count1.process()
except Exception as a:
    print(f"invalid input {a}")
finally:
    print("exit")
