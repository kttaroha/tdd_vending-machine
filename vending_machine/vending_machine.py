from typing import List, Dict


class VendingMachine:
    def __init__(self):
        self.money_box = {10: 0, 50: 0, 100: 0, 500: 0, 1000: 0}
        self.juice_box = {"coke": {"price": 120, "num": 5}}

    def insert(self, money: List[int]) -> List[int]:

        invalid_money = []
        for m in money:
            if not self.validate_money(m):
                invalid_money.append(m)
            else:
                self.money_box[m] += 1

        return invalid_money

    def validate_money(self, money) -> bool:
        return money in self.money_box.keys()

    # TODO: コメントが足りない！
    def get_amount(self) -> int:
        return sum([k * v for k, v in self.money_box.items()])

    def refund_money(self) -> Dict[int, int]:
        money_box = self.money_box
        self.money_box = {k: 0 for k in self.money_box.keys()}
        return money_box

    def get_juice_info(self) -> Dict[str, Dict]:
        return self.juice_box

