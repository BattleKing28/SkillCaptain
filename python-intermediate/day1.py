class BankAccount:
    def __init__(self, account_number, account_holder_name, account_balance):
        if (
            self.validate_inputs(account_number, account_holder_name, account_balance)
            == True
        ):
            self.account_number = account_number
            self.account_holder_name = account_holder_name
            self.account_balance = account_balance
        else:
            print("Please enter supported values")

    def deposit_money(self, amountToDeposit):
        if amountToDeposit < 1:
            print(f"Cannot add {amountToDeposit} amount")
            return

        try:
            self.account_balance += amountToDeposit
        except Exception as err:
            print(err)
            return
        print(
            f"Successfully deposited {amountToDeposit} in your account, your new balance is {self.account_balance}"
        )

    def withdraw_money(self, amountToWithdraw):
        if amountToWithdraw < 1 or amountToWithdraw > self.account_balance:
            print(f"Cannot withdraw {amountToWithdraw} amount")
            return
        try:
            self.account_balance -= amountToWithdraw
        except Exception as err:
            print(err)
            return

        print(
            f"Successfully withdrawn {amountToWithdraw} from your account, your new balance is {self.account_balance}"
        )

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder name: {self.account_holder_name}")
        print(f"Account Balance: {self.account_balance}")

    @staticmethod
    def validate_inputs(account_number, account_holder_name, account_balance):
        if (
            isinstance(account_number, int)
            and isinstance(account_holder_name, str)
            and isinstance(account_balance, int)
        ):
            return True
        else:
            return False

    pass


account1 = BankAccount(225414, "Mark", 5000)
account1.deposit_money(100)
account1.withdraw_money(10000)
# account1.withdraw_money(100)
account1.display_account_info()
