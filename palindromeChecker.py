class palindrome():
    def getdata(self):
        self.value=input("Enter:")
    def process(self):
        self.p=self.value[::-1]
        if self.p==self.value:
            print("it's a palindrome")
        else:
            print("it's not a palindrome")
value1=palindrome()
value1.getdata()
value1.process()