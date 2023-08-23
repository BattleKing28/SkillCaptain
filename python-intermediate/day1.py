class BankAccount:
    def __init__(self, accountNumber, accountHolderName, accountBalance):
        if (
            self.validateInputs(accountNumber, accountHolderName, accountBalance)
            == True
        ):
            self.accountNumber = accountNumber
            self.accountHolderName = accountHolderName
            self.accountBalance = accountBalance
        else:
            print("Please enter supported values")

    def depositMoney(self, amountToDeposit):
        if amountToDeposit < 1:
            print(f"Cannot add {amountToDeposit} amount")
            return

        try:
            self.accountBalance += amountToDeposit
        except Exception as err:
            print(err)
            return
        print(
            f"Successfully deposited {amountToDeposit} in your account, your new balance is {self.accountBalance}"
        )

    def withdrawMoney(self, amountToWithdraw):
        if amountToWithdraw < 1 or amountToWithdraw > self.accountBalance:
            print(f"Cannot withdraw {amountToWithdraw} amount")
            return
        try:
            self.accountBalance -= amountToWithdraw
        except Exception as err:
            print(err)
            return

        print(
            f"Successfully withdrawn {amountToWithdraw} from your account, your new balance is {self.accountBalance}"
        )

    def displayAccountInfo(self):
        print(f"Account Number: {self.accountNumber}")
        print(f"Account Holder name: {self.accountHolderName}")
        print(f"Account Balance: {self.accountBalance}")

    def validateInputs(self, accountNumber, accountHolderName, accountBalance):
        if (
            type(accountNumber) == int
            and type(accountHolderName) == str
            and type(accountBalance) == int
        ):
            return True
        else:
            return False

    pass


account1 = BankAccount(225414, "Mark", 5000)
account1.depositMoney(100)
# account1.withdrawMoney(0)
account1.withdrawMoney(100)
account1.displayAccountInfo()
