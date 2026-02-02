try:
 class largestnum:
    def getdata(self):
      self.num=[]
      for i in range(1,4):
        self.num.append(int(input(f"Enter the number {i}:")))
      print(self.num)
    def process(self):
     if self.num[0]>self.num[1]and self.num[0]>self.num[2]:
      print(f"{self.num[0]} is Largest")
     elif self.num[1]>self.num[0] and self.num[1]>self.num[2]:
      print(f"{self.num[1]} is Largest")
     else:
      print(f"{self.num[2]} is Largest")
      
 n=largestnum()
 n.getdata()
 n.process()
except Exception as a:
    print(f"invallid option {a}")
finally:
    print("done")
      
