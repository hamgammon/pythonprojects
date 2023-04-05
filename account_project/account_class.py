#create the class called 'Account'
class Account:

#tip - class var for a auto incament id.  
    __account_id_next = 1 #make it 1 and add one for each new a/c? for auto inc (come back to this)

 #I want to get the info from the user - name needs to be length checked - if wrong raise runtime error and we need a balance 
    def __init__(self, name, balance = 0):
        self._account_id = Account.__account_id_next
        Account.__account_id_next += 1
        self.name = name
        self.balance = balance
        
#PRODUCTION - Add name- use a setter to check name is correct length - also raise a runtime error to inform the user that its wrong in to between 4 and 15 chars.
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        try:
            if not (4 <= len(value) <= 15):
                raise RuntimeError("Name should be between 4 and 15 characters")
            else:
                self._name = value
        finally:
            print('***test message finally***')

####-- Depostit and Withdraw methods------------------------------------------------------------------
#need to add and withdraw money "methods" - (confirm termonolgy again)
#Deposit - Action of adding money to an account - Check account_id and add money to it.
#Withdrawal - Action of subtracting money from an account      

    # @property
    # def balance(self) -> float:
    #     return self.__balance
    
    #Deposit - Action of adding money to an account - Check account_id and add money to the existing balance of account.

    def deposit(self, amount: float):
        if amount < 0:
            print("\n***Error - You can only deposit a positive amount***")
        else:
            self.balance += amount
            print(f"\n***Deposited {amount} successfully***")

    #Withdrawal - Action of subtracting money from an account  - Check account_id and remove money from the existing balance of account    

    def withdraw(self, amount: float):
        if amount < 0:
            print("\n***Error - Please enter a positive amount***")

        elif self.balance < amount:
            print("\n***Sorry - Insufficient balance!***")

        else:
            self.balance -= amount
            print(f"\n***Withdrawn {amount} successfully")


#PRODUCTION - display account details to the user 
    def displayAccountDetails(self):
        print(f'Account details:\nName - {self.name}, Balance - {self.balance}')



#####TESTING#########----------------------------------------------------------------------------

#TESTING? - display details TESTING - dont want to show user id
    def displayAccountDetailsTest(self):
        print(f'Account details:\nId - {self._account_id}, Name - {self.name}, Balance - {self.balance}')

#TESTING - display ammount of accounts for testing -
    def displayTotalAccount(self):
        print(f'Number of accounts: ', Account.__account_id_next)

if __name__ == '__main__':
    
    a1 = Account(name = 'Scott', balance= '10')
    a1.displayAccountDetailsTest()
    #a1.displayTotalAccount()

    a2 = Account(name = 'Matt', balance= '20')
    a2.displayAccountDetailsTest()
    a2.displayTotalAccount()

    a2.displayAccountDetailsTest()



