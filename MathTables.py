class tables:
    def getdata(self):
        self.n=int(input("Enter the number:"))
        
    def process(self):
        for i in range(1,11):
          print(f"{i}*{self.n}={i*self.n}")
          
execute=tables()
execute.getdata()
execute.process()
        
            