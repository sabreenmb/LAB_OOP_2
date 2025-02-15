class BankAccount:
    def __init__(self,username:str ,pin:str,account_holder:str,balance:int=0):
        self.__username=username
        self.__pin=pin
        self.__set_name(account_holder)
        self.__set_balance(balance)

    #setters
    def __set_name(self,account_holder:str):
        if not account_holder.isalpha:
            raise Exception("Name can only contains charecters")
        self.__account_holder=account_holder

    def __set_balance(self, balance:int):
        if not isinstance(balance,int):
            raise Exception("balance can only be numbers")
        self.__balance=int(balance)

    def deposit(self, amount:int):
        if not isinstance(amount,int):
            raise Exception ("invalid input the amont should be nummbers only")
        if amount<=0:
            raise Exception("the amount can be only greater than 0")
        self.__balance+=amount
    
    def withdraw(self, amount:int):
        if not isinstance(amount,int):
            raise Exception ("invalid input the amont should be nummbers only..")
    
        if self.__balance>=amount:
            self.__balance-=amount
        else:
            raise Exception("Sorry the withdraw failed, there is no sufficient funds in the account.")
    
    #getters
    def get_balance(self)->int:
        return self.__balance
    
    def get_account_holder(self)->str:
        return self.__account_holder
    
    def get_username(self)->str:
        return self.__username
    
    def get_user_info(self)->dict:
        return {"pin": self.__pin,
                "account_holder": self.__account_holder,
                "balance": self.__balance}

    
    

    
