class tables:
    def getdata(self):
        self.num=int(input("Enter the number:"))
        
    def process(self):
        for i in range(1,11):
          print(f"{i}*{self.num}={i*self.num}")
          
execute=tables()
execute.getdata()
execute.process()
        
            