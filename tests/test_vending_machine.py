from vending_machine.vending_machine import VendingMachine


def test_check_multiple_insert():
    """複数のお金が挿入できるか"""

    vending_machine = VendingMachine()
    insert_money = [10, 50, 100, 500, 1000]
    actual_insert = vending_machine.insert(insert_money)

    assert actual_insert == []

    actual_money_box = vending_machine.money_box
    expected = {10: 1, 50: 1, 100: 1, 500: 1, 1000: 1}

    assert actual_money_box == expected


def test_insert_invalid_money():
    """無効なお金が投入された物がそのまま返却されるか"""

    vending_machine = VendingMachine()
    insert_money = [1, 5, 10000, 3]

    actual = vending_machine.insert(insert_money)
    expected = insert_money
    assert actual == expected


def test_get_amount():
    """自販機に投入した金額の総計が正しく出力されるか"""

    vending_machine = VendingMachine()
    insert_money = [10, 50, 100, 500, 1000]
    vending_machine.insert(insert_money)

    actual = vending_machine.get_amount()
    expected = sum(insert_money)

    assert actual == expected


def test_refund_money():
    """自販機に入っているお金が正しく返金されるか"""

    vending_machine = VendingMachine()
    insert_money = [10, 50, 100, 500, 1000]
    vending_machine.insert(insert_money)

    actual_refunded_money = vending_machine.refund_money()
    expected_refunded_money = {10: 1, 50: 1, 100: 1, 500: 1, 1000: 1}

    assert actual_refunded_money == expected_refunded_money

    actual_amount = vending_machine.get_amount()
    expected_amount = 0

    assert actual_amount == expected_amount


def test_get_juice_info():
    """自販機で管理されているジュースの情報を取得する"""

    vending_machine = VendingMachine()

    actual = vending_machine.get_juice_info()
    expected = {"coke": {"price": 120, "num": 5}}

    assert actual == expected
