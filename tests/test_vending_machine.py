from vending_machine.vending_machine import VendingMachine


def test_check_money():
    vending_machine = VendingMachine()
    insert_money = 10
    vending_machine.insert(insert_money)

    actual = vending_machine.money_box
    expected = {10: 1, 50: 0, 100: 0, 500: 0, 1000: 0}

    assert actual == expected


def test_check_multiple_insert():
    vending_machine = VendingMachine()
    insert_money = [10, 50, 100, 500, 1000]
    vending_machine.insert(insert_money)

    actual = vending_machine.money_box
    expected = {10: 1, 50: 1, 100: 1, 500: 1, 1000: 1}

    assert actual == expected


def test_get_amount():
    vending_machine = VendingMachine()
    insert_money = [10, 50, 100, 500, 1000]
    vending_machine.insert(insert_money)

    actual = vending_machine.get_amount()
    expected = sum(insert_money)

    assert actual == expected


def test_refund_money():
    vending_machine = VendingMachine()
    insert_money = [10, 50, 100, 500, 1000]
    vending_machine.insert(insert_money)

    actual_refunded_money = vending_machine.refund_money()
    expected_refunded_money = {10: 1, 50: 1, 100: 1, 500: 1, 1000: 1}

    assert actual_refunded_money == expected_refunded_money

    actual_amount = vending_machine.get_amount()
    expected_amount = 0

    assert actual_amount == expected_amount

def test_insert_invalid_money():
    vending_machine = VendingMachine()
    insert_money = [1, 5, 10000, 3]
    
    actual = vending_machine.insert(insert_money)
    expected = insert_money
    assert actual == expected


