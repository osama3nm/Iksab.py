class BankAccount :
    customers = 0
    total_savings = 0        # اجمالي المدخرات 
    def __init__(self,id=2024255465,balance=0,iban=5478-8569-5847-9658):      # iban : number of bank account like(5478-8569-5847-9658)
        self.__id = id
        self.__balance = balance         
        self.__iban = iban
        BankAccount.customers += 1
        BankAccount.total_savings +=balance

    def set_id(self,id):
        self.__id = id 
    def get_id(self):
        return self.__id
    
    def deposit(self,balance):        # ايداع
        if balance <= 0 :
            print("ما بزبط اودع بالحساب صفر او اقل من صفر ❎")
            return True
        else :
            self.__balance += balance 
            BankAccount.total_savings += balance
            return True

    def withdraw(self,balance):       # سحب 
        if balance > self.__balance :
            print("الرصيد اقل من عمليه سحبك")
            return False 
        elif balance <= 0 :
            print("لازم تسحب مصاري بزبطش تسحب صفر او قيمه سالبه")
            return False
        else :
            print("تم السحب بنجاح ✅")  
            self.__balance -= balance  
            BankAccount.total_savings -= balance
            return True



    def display_balance(self):
        return self.__balance
    
    def set_iban(self,iban):
        self.__iban = iban
    def get_iban(self):
        return self.__iban
    
# customer 1
customer1 = BankAccount(balance=100)     # بزبط احدد متغير واحد واوديلو قيمو من خلال انو احط اسم هاض المتغير 
print(customer1.get_id())
print(customer1.display_balance())
customer1.deposit(-20)
print(f"totally balance of customer 1 : {customer1.display_balance()}")


# customer 2
customer2 = BankAccount(2044568,100,2556-9665-5447-7885)
customer2.deposit(1000)
customer2.deposit(-180)
customer2.deposit(55)
print(f"totally balance of customer 2 : {customer2.display_balance()}")



print(f"number of Customers is : {BankAccount.customers}")
print(f"Total savings is : {BankAccount.total_savings}")


