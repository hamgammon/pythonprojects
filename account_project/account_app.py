#point 1 error handling/expetion (try etc)
#point 4 warning neg value
#point 5 error message to user 
#write account class and then usage

#import the class
from account_class import Account

accounts: dict[int, Account] = {}  # dictionary to store accounts by account_id

#While loop for main menu
while True:
    #Main menu with options needed
    print("\nMain Menu")
    print("1. Create New Account")
    print("2. Use Existing Account")
    print("3. Quit\n")
    choice = input("Enter your choice (1-3): ")
    
    #Create an account - need to check that errors are being handled as per spec doc 
    if choice == "1":
        #capture details from the user - name and starting balance
        name = input("Enter name (4-15 characters): ")
        #do i check the 4-15 requirement here?? i think in class
        balance = float(input("Enter initial balance: "))
        #details in
        account = Account(name, balance)
        accounts[account._account_id] = account

        #New account created message showing ID to user
        print(f"\n***{account._name} your account has been created with ID {account._account_id} ***")
        print(f"***Please use this ID for future transactions on your account.***")
    
    #Exisiting Accounts menu option
    elif choice == "2":
        #capture account id
        account_id = int(input("Enter account ID: "))
        
        #if account_id exists 
        if account_id in accounts:
            account = accounts[account_id]
            #if account_id exists then show account menu
            while True:
                print("\nAccount Menu")
                print("1. Get Account Details")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Back To Main Menu")
                #capture user options
                choice = input("Enter your choice (1-4): ")
                
                #Op 1 - display account details as per the class
                if choice == "1":
                    print('\n')
                    account.displayAccountDetails()
                
                #op 2 - disposit funds option
                elif choice == "2":
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)
                
                #op 3 - withdraw funds
                elif choice == "3":
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                
                #op 4 'go back' - break out this if and go back to above if
                elif choice == "4":
                    break 
                else:
                    print("\n**Invalid choice - Please try again**")
        
        #if account_id doesnt exist, inform user
        else:
            print("Account not found")
    
    #quit the program
    elif choice == "3":
        #exit the program
        break 
    
    #inform user that option is invalid
    else:
        print("\n**Invalid choice - Please try again**")
        