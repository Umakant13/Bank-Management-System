import json
import random
import string
from pathlib import Path


class Bank:
    
    database = 'Mega Project 2 - Bank Management/data.json'
    data =[]
    
    try:
        
        if Path(database).exists():
            
            with open(database, "r")as f:
                data = json.loads(f.read())
        else:
            print("No such file exists")
            
    except Exception as e:
        print(f"An exception occured as {e}")
        
    @classmethod
    def __update(cls):
        with open(cls.database, "w") as f:
            f.write(json.dumps(Bank.data))
        
    @classmethod
    def __accountGenerate(cls):
        alphabets = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=8)
        spchar = random.choices("!@#%$^&*", k=1)
        
        id=alphabets + num+ spchar
        random.shuffle(id)
        return "".join(id)
    
        
    def createAccount(self):
        info = {
            "name" : input("Tell Your Name :-"),
            "age" : int(input("Tell Your Age :-")),
            "email" : input("Tell Your Email :-"),
            "pin" : int(input("Tell Your 4 Number Pin :-")),
            "accountNo" : Bank.__accountGenerate(),
            "balance" : 0
        }
        
        if info['age'] < 18 or len(str(info['pin'])) !=4:
            print("Sorry you cannot create your account")
        
        else:
            print("Your account has been created successfully")
            
            for i in info:
                print(f"{i} : {info[i]}")
            
            print("Please note down your account number")
            
            Bank.data.append(info)
            
            Bank.__update()
            
    def depositMoney(self):
        accountNumber = input("Please tell me your account number :-")
        pin = int(input("Please tell your pin number :-"))
        
        
        userData = [i for i in Bank.data if i['accountNo'] == accountNumber and i['pin'] == pin]
        
        if userData == False:
            print("Sorry, no data found")
        else:
            amount = int(input("How much amount you want to deposit :-"))
            
            if amount >= 10000 or amount < 0:
                print("Sorry the amount is too much you can deposit below 10000 and above 0")
            
            else:
                userData[0]['balance'] +=amount
                Bank.__update()
                print("Amount deposited successfully ")
                
    
    def withdrawMoney(self):
        accountNumber = input("Please tell me your account number :-")
        pin = int(input("Please tell your pin number :-"))
        
        userData = [i for i in Bank.data if i["accountNo"] == accountNumber and i["pin"] == pin]
        
        if userData == False:
            print("Sorry, no data found")
        
        else:
            amount = int(input("How much amount you want to withdraw :-"))
            
            if userData[0]['balance'] < amount:
                print("Sorry you don't have that much money")
            else:
                
                userData[0]['balance'] -= amount
                Bank.__update()
                print("Amount withdraw successfully")
    
    def showDetails(self):
        accountNumber = input("Please tell me your account number :-")
        pin = int(input("Please tell your pin number :-"))
        
        userData = [i for i in Bank.data if i['accountNo'] == accountNumber and i['pin'] ==pin]
        
        print("Your details are as follows: \n\n\n ")
        
        for i in userData[0]:
            print(f"{i} : {userData[0] [i]}")
    
    
    def updateDetails(self):
        accountNumber = input("Please tell me your account number :-")
        pin = int(input("Please tell your pin number :-"))
        
        userData = [i for i in Bank.data if i['accountNo'] == accountNumber and i['pin'] ==pin]
        
        if userData == False:
            print("No such user found")
        
        else:
            print("You cannot change the age, account number, balance")
            
            print("Fill the details for change or leave it empty if no change")
            
            newData = {
                "name" : input("Please enter your name or press enter :-"),
                "email" : input("Please enter you new email or press enter :-"),
                "pin" : input("Please enter new pin or press enter :- ")
                
            }
            
            if newData["name"] == "":
                newData["name"] = userData[0]["name"]
            
            if newData["email"] == "":
                newData["email"] = userData[0]["email"]
            
            if newData["pin"] == "":
                newData["pin"] = userData[0]["pin"]
            
            newData["age"] = userData[0]["age"]
            newData["accountNo"] = userData[0]["accountNo"]
            newData["balance"] = userData[0]["balance"]
            
            if type(newData["pin"]) == str:
                newData["pin"] = int (newData["pin"])
            
            for i in newData:
                if newData[i] == userData[0][i]:
                    continue
                else:
                    userData[0][i] = newData[i]
                    
            Bank.__update()
            print("User details updated successfully")
            
            
            
    def deleteAccount(self):
        accountNumber = input("Please tell me your account number :-")
        pin = int(input("Please tell your pin number :-"))
        
        userData = [i for i in Bank.data if i['accountNo'] == accountNumber and i['pin'] ==pin]
        
        if userData == False:
            print("No such user found")
        else:
            check = input("Press Y if you actually want to delete the account or Press N :-")
            
            if check == "n" or check == "N":
                print("By Pass")
            
            else:
                index = Bank.data.index(userData[0])
                Bank.data.pop(index)
                print("Account deleted successfully")
                Bank.__update()
                
                
user = Bank()

print("Press 1 for creating an account")
print("Press 2 to Deposit the money in the bank")
print("Press 3 to withdraw the money")
print("Press 4 to get details")
print("Press 5 to update the details")
print("Press 6 to delete the account")

check =int(input("Tell me your response :-"))

if check ==1:
    user.createAccount()

if check==2:
    user.depositMoney()
    
if check==3:
    user.withdrawMoney()

if check==4:
    user.showDetails()
    
if check==5:
    user.updateDetails()
    
if check==6:
    user.deleteAccount()