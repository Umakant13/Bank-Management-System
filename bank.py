import json
import random
import string
from pathlib import Path


class Bank:
    database = Path("data.json")
    data = []

    # Load database
    if database.exists():
        with open(database, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    @classmethod
    def __update(cls):
        with open(cls.database, "w", encoding="utf-8") as f:
            json.dump(cls.data, f, indent=4)

    @staticmethod
    def __accountGenerate():
        alphabets = random.choices(string.ascii_uppercase, k=3)
        digits = random.choices(string.digits, k=8)
        special = random.choice("!@#$%^&*")
        account_id = alphabets + digits + [special]
        random.shuffle(account_id)
        return "".join(account_id)

    @classmethod
    def createAccount(cls, name, age, email, pin):
        if age < 18:
            return {"error": "You must be 18+ to create an account"}
        if len(str(pin)) != 4:
            return {"error": "PIN must be 4 digits"}

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": cls.__accountGenerate(),
            "balance": 0
        }

        cls.data.append(info)
        cls.__update()
        return {"success": "Account created successfully", "account": info}

    @classmethod
    def __findUser(cls, accountNo, pin):
        return next((i for i in cls.data if i["accountNo"] == accountNo and i["pin"] == pin), None)

    @classmethod
    def depositMoney(cls, accountNo, pin, amount):
        user = cls.__findUser(accountNo, pin)
        if not user:
            return {"error": "Invalid account or PIN"}
        if amount <= 0 or amount > 10000:
            return {"error": "Deposit must be between 1 and 10000"}

        user["balance"] += amount
        cls.__update()
        return {"success": f"{amount} deposited", "balance": user["balance"]}

    @classmethod
    def withdrawMoney(cls, accountNo, pin, amount):
        user = cls.__findUser(accountNo, pin)
        if not user:
            return {"error": "Invalid account or PIN"}
        if amount <= 0:
            return {"error": "Withdrawal must be positive"}
        if user["balance"] < amount:
            return {"error": "Insufficient funds"}

        user["balance"] -= amount
        cls.__update()
        return {"success": f"{amount} withdrawn", "balance": user["balance"]}

    @classmethod
    def showDetails(cls, accountNo, pin):
        user = cls.__findUser(accountNo, pin)
        if not user:
            return {"error": "Invalid account or PIN"}
        return {"success": user}

    @classmethod
    def updateDetails(cls, accountNo, pin, name=None, email=None, newPin=None):
        user = cls.__findUser(accountNo, pin)
        if not user:
            return {"error": "Invalid account or PIN"}

        if name:
            user["name"] = name
        if email:
            user["email"] = email
        if newPin and len(str(newPin)) == 4:
            user["pin"] = newPin

        cls.__update()
        return {"success": "Details updated", "account": user}

    @classmethod
    def deleteAccount(cls, accountNo, pin):
        user = cls.__findUser(accountNo, pin)
        if not user:
            return {"error": "Invalid account or PIN"}

        cls.data.remove(user)
        cls.__update()
        return {"success": "Account deleted"}
