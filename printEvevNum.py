try:
 class eve:
     def getdata(self):
        self.num=int(input("enter the number:"))
        
     def process(self):
        for i in range(1,self.num+1):
            if i %2==0:
                print(i)
 num1=eve()
 num1.getdata()
 num1.process()
except Exception as e:
    print( f"invalid option {e}")
finally:
    print("done")
