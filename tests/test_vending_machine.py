from vending_machine.vending_machine import VendingMachine


def test_check_coins():
    vending_machine = VendingMachine()
    insert_coins = 10
    vending_machine.insert(insert_coins)

    actual = vending_machine.coins
    expected = {10: 1, 50: 0, 100: 0, 500: 0, 1000: 0}

    assert actual == expected


def test_check_multiple_insert():
    vending_machine = VendingMachine()
    insert_coins = [10, 50, 100, 500, 1000]
    vending_machine.insert(insert_coins)

    actual = vending_machine.coins
    expected = {10: 1, 50: 1, 100: 1, 500: 1, 1000: 1}

    assert actual == expected
