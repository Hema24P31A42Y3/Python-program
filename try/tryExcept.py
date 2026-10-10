def values(a,b):
       if a>10 and b<100:
          print(a,b)
       else:
           try:
               print ("errr")
           except ZeroDivisionError:
               print("cant find")
           finally:
               print("i get it")
