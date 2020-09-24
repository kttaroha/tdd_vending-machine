class VendingMachine:
    def __init__(self):
        self.coins = {10: 0, 50: 0, 100: 0, 500: 0, 1000: 0}

    def insert(self, coin):
        if type(coin) == int:
            self.coins[coin] += 1
        elif type(coin) == list:
            for c in coin:
                self.coins[c] += 1
