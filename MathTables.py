try: 
 class tables:
    def getdata(self):
        self.n=int(input("Enter The Number:"))
        
    def process(self):
        for i in range(1,11):
          print(f"{i}*{self.n}={i*self.n}")
          
 execute=tables()
 execute.getdata()
 execute.process()
except Exception as a:
    print(f"Invalid option {a}")
finally:
    print("exit")
        
            