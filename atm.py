pin = int(input("Enter your pin number: "))
balance = 60000
if pin == 1234:
   print("Welcome to ut bank")
   print("""
         1.check balance
         2.deposite
         3.withdraw
         4.help
         """)
   options = int(input("Enter your options(1 to 4): "))
   if options == 1:
       print("your current balance is ",balance,"Rs/-")
   elif options == 2:
       deposite_amount = float(input("enter your deposite amount:"))
       if deposite_amount <= 100000:
           balance = deposite_amount + balance
           print(" your updated balance is :" ,balance, "Rs/-")
       else:
           print("your daily limit is 100000")
   elif options == 3:
       withdraw_amount = int(input("enter your deposite amount:"))
       if withdraw_amount <= balance:
          balance = balance -  withdraw_amount
          print("your updated balance is :",balance,"Rs/-") 
       else :
          print("Insufficient balance.your balance: ",balance,"Rs/-")
   elif options == 4:
       print("welcome to help center , for any questions please contact 0000123")
else:
   print("Incorrect pin number")
