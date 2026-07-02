class BankAccount :
    customers = 0
    total_savings = 0        # اجمالي المدخرات 
    def __init__(self,id=2024255465,balance=0,iban=5478-8569-5847-9658):      # iban : number of bank account like(5478-8569-5847-9658)
        self.__id = id
        self.__balance = balance         
        self.__iban = iban
        BankAccount.customers += 1

    def set_id(self,id):
        self.__id = id 
    def get_id(self):
        return self.__id
    
    def set_balance(self,balance):
        self.__balance += balance 
        BankAccount.total_savings += balance


    def get_balance(self):
        return self.__balance
    
    def set_iban(self,iban):
        self.__iban = iban
    def get_iban(self):
        return self.__iban
    
# customer 1
customer1 = BankAccount(balance=100)     # بزبط احدد متغير واحد واوديلو قيمو من خلال انو احط اسم هاض المتغير 
print(customer1.get_id())
print(customer1.get_balance())
customer1.set_balance(-20)
print(f"totally balance of customer 1 : {customer1.get_balance()}")


# customer 2
customer2 = BankAccount(2044568,100,2556-9665-5447-7885)
customer2.set_balance(1000)
customer2.set_balance(-180)
customer2.set_balance(55)
print(f"totally balance of customer 2 : {customer2.get_balance()}")



print(f"number of Customers is : {BankAccount.customers}")
print(f"Total savings is : {BankAccount.total_savings}")


