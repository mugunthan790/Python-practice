try:
 def fun(n):
    if n == 0:
        return 0  
    return (n % 10) + fun(n // 10)
 n=1234
 print(fun(n))
 
except Exception as e:
    print(f"Invallid Option{e}")
finally:
    print("exit")