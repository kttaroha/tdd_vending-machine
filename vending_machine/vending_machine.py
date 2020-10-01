class VendingMachine:
    def __init__(self):
        self.money_box = {10: 0, 50: 0, 100: 0, 500: 0, 1000: 0}

    def insert(self, money):
        invalid_money = []
        if type(money) == int:
            if not validate_money(money):
                invalid_money.append(money)
            else:
                self.money_box[money] += 1
        elif type(money) == list:
            for m in money:
                validate_money(m)
                self.money_box[m] += 1

        return invalid_money

        # TODO: listとint以外も考慮する

    def validate_money(self, money):

        
    # TODO: コメントが足りない！
    def get_amount(self):
        return sum([k * v for k, v in self.money_box.items()])

    # 返ってくるのdictってわかりづらい？

    def refund_money(self):
        money_box = self.money_box
        self.money_box = {k: 0 for k in self.money_box.keys()}
        return money_box

