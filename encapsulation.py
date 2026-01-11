# Example WITHOUT encapsulation (unsafe)

class bankaccount:
    def __init__(self, balance):
        self.balance = balance   # public variable


# Creating an object
rishabhAC = bankaccount(3000)   # initial balance is 3000
rishabhAC.balance = 4000        # balance changed directly from outside
print(rishabhAC.balance)


'''
Output:
4000
'''

# --------------------------------------------------
# Example WITH encapsulation (safe)
# --------------------------------------------------

class bankaccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def get_balance(self):
        return self.__balance      # controlled access


# Creating an object
rishabhAC = bankaccount(3000)

# Trying to change balance directly (this will NOT affect the real balance)
rishabhAC.__balance = 4000

# Accessing balance using a method
print(rishabhAC.get_balance())


'''
Output:
3000
'''
