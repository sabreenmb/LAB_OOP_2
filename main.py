from account import BankAccount 
import json

print("-"*20,"Welcome to MBS Bank System","-"*20)
print("---Login")

file_name="mbs_bank.json"
all_users={}

def login()->BankAccount:
    attempt=3
    while attempt!=0:
        attempt-=1
        try:
            username=input("Username: ")
            password=input("Password: ")
            if username.isspace() or password.isspace():
                raise Exception("please enter a valid input")
            else:
                account=load_user_data(file_name,username,password)
        except Exception as error:
            print(error)
        else:
            break
    else:
        raise Exception("You have reached the maximum number of attempts. Please try again later.")
    return account

def load_user_data(filename,user,pin)->BankAccount:
    global all_users
    try:
        with open(filename, "r", encoding="utf-8") as json_file:
            # content = json_file.read()
            # all_users=json.loads(content)
            all_users= json.load(json_file)
            if user in all_users:
                if pin==all_users[user]["pin"]:
                    account=BankAccount(user,pin,all_users[user]["account_holder"],all_users[user]["balance"])
                    return account
                
            raise Exception("invalid username or passward please try again")
            
    except (FileNotFoundError, json.JSONDecodeError):
        print("something went wrong please try again later")

def update_user_data(filename,all_users,account):
    all_users[account.get_username()]=account.get_user_info()
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(all_users, json_file, indent=4)
    

menu='''
1-Dispay account balance
2-Deposite
3-Withdraw
4-Exit
'''

try:
    account =login()

    print("-"*10,f"How can we help you {account.get_account_holder()}","-"*10)
    while True:
        try:
            user_choice= input(menu+"\nEnter your choice:")
            print("-"*40)
            if(user_choice=="1"):
                print(f"The account balance is : {account.get_balance()}")
                input()
            elif user_choice=="2":
                value=input("Enter the amount: ")
                account.deposit(int(value))
                print("The amount has been added successfully")
                print(f"The account balance is :{account.get_balance()}")
                input()
            elif user_choice=="3":
                print(f"The current balance is :{account.get_balance()}")

                value=input("Enter the amount: ")
                account.withdraw(int(value))
                print("The amount has been withdraw successfully")

            elif user_choice=="4":
                print("Thank you for choosing MBS Bank")
                break
            else:
                raise TypeError("invalid input.. try again")
        except ValueError :
            print("invalid input the amont should be nummbers only,")
        except TypeError as error:
            print(error)             
        except Exception as error:
            print(error)
            
except Exception as error:
        print(error)
else:
    update_user_data(file_name,all_users,account)









