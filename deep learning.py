print("====encapsulation====")


class account():
    description = "this class is for making bank accounts"

    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    def get_balance(self):
        print(f"owner {self.__owner} has balance {self.__amount} usd.")

    def deposit(self, amount):
        print("++ deposit ++:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("---withdraw---:", amount)
        self.__amount -= amount


my_account = account("bekmirza", 49000)
my_account.get_balance()
my_account.deposit(300050)
my_account.withdraw(50)
my_account.get_balance()
print("---------")
try:
    result = my_account.__amount
    print("result:", result)
except AttributeError as err:
    print("Error:", err)
