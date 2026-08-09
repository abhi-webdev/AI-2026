
class ChaiOrder :
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def describe(self) :
        return f"{self.size} ml of {self.type} chai"

order = ChaiOrder("Masala", 200)
print(order.describe())

order_2 = ChaiOrder("Ginger Chai", 150)
print(order_2.describe())

# -------- Pizza Factory ---------------

class PizzaFactory :
    pizaSize = ["Large", "Medium", "Small"]
    def __init__(self, pizaType, pizaSize):
        if pizaSize not in self.pizaSize :
            raise ValueError("Pizza size must be Large, Medium, or Small")
        
        self.type = pizaType
        self.size = pizaSize

    def serve(self) :
        return f"{self.size} size of {self.type} pizza served"

serving_1 = PizzaFactory("Onion", "Large")

print(serving_1.serve())


# -------- Account Balance Checker --------------

class Account :
    account_type = ["Saving", "Current"]
    def __init__(self, account_holder, account_type, balance):
        if account_type not in self.account_type :
            raise ValueError("Account must be saving or current")

        self.account_holder = account_holder
        self.account_type = account_type
        self.balance = balance

    def describe (self) :
        return f"{self.account_type} account has {self.balance} balance. Whose owner is {self.account_holder}"

    def deposite(self, amount) :
        self.balance = self.balance + amount
        return f"Total Balance {self.balance}"

    def withdraw(self, amount) :
        if self.balance > amount :
            self.balance = self.balance - amount
            return f"Remaining balance {self.balance}"

account_details = Account("Abhimanyu", "Saving", 5000)

print(account_details.describe())

print(account_details.deposite(amount=500))
print(account_details.withdraw(amount=300))

print(account_details.withdraw(amount=1000))

print(account_details.deposite(200))

