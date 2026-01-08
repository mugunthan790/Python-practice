try:
 class palindrome():
    def getdata(self):
        self.v=input("Enter:")
    def process(self):
        self.p=self.v[::-1]
        if self.p==self.v:
            print(f"{self.p} is palindrome")
        else:
            print(f"{self.p} is not a palindrome")
 value1=palindrome()
 value1.getdata()
 value1.process()
except Exception as a :
    print(f"invalid option {a}")
finally:
    print("exit")