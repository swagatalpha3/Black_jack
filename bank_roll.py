class BankRoll():

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"Total balance in your account is {self.amount} Euros"

    def bet(self, bet_amount):
        if bet_amount <= self.amount:
            self.amount -= bet_amount
            print(f"{bet_amount} Euros deducted from your account")
            print(f"Total balance in your account is {self.amount} Euros")

        else:
            print('You have insufficient balance')
            print(f"Total balance in your account is {self.amount} Euros")
        return self.amount

    def win(self, win_amount):
        self.amount += win_amount
        print(f"{win_amount} Euros added to your account")
        print(f"Total balance in your account is {self.amount} Euros")


if __name__ == "__main__":
    player1 = BankRoll(100)
    player2 = BankRoll(200)
    player2.bet(20)
    print(player1)
    print(player2)
    player2.win(40)
    print(player2)
