class Atm():
    def __init__(self,pin_num):
        self.pin_num = pin_num
        if pin_num == 1234:
            print("Welcome hs bank")
        else:
            print("wrong pin")
    def balance(self,check_balance):
        self.check_balance=check_balance
        return f"your bank balance ={check_balance}"
    def show_balance(self):
        return f"bank balance={self.check_balance}"
    def withdraw(self,withdraw_amount):
        self.withdraw_amount=withdraw_amount
        self.check_balance=self.check_balance-withdraw_amount
        return f"available balance={self.check_balance}"
    def deposite(self,deposite_amount):
        self.deposite_amount=deposite_amount
        if deposite_amount <=100000:
            self.check_balance=self.check_balance+deposite_amount
            return f"bank balance ={self.check_balance}"
        else:
            return "daily limit exceeded"
    def new_pin(self,new_pin):
        self.new_pin=new_pin
        self.pin_num=new_pin
        return f"new pin:{new_pin}"
hema=Atm(1234)
hema.balance(30000)
hema.show_balance()
hema.deposite(87000)
hema.new_pin(2345)
        
        
