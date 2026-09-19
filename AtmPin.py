count = 3
for i in range(1,4):
    pin = int (input("Enter pin number"))
    if pin == 1234:
        print("Welcome ut bank")
        break
    else:
        count = count -1
        if count > 0:
            print("try again letter")
            print("attempts left :",count)
        else:
            print("acount blocked")
            
