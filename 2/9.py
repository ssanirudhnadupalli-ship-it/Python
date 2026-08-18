class BankAccount:
    def __init__(self, holder_name, account_number):
        self.holder_name = holder_name
        self.account_number = account_number

acc1 = BankAccount("Harsha", "123456789")
print("Account Holder:", acc1.holder_name, "Account Number:", acc1.account_number)
