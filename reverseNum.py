try:
 class rev:
    def getdata(self):
        self.num=(input("Enter the number:"))
    def process(self):
        self.reverse=self.num[::-1]
    def display(self):
        print(f"Reverse num is : {self.reverse}")
 num1=rev()
 num1.getdata()
 num1.process()
 num1.display()
except Exception as e:
    print(f"Invalid option {e}")
finally:
    print("Exit")