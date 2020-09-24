from vending_machine.vending_machine import VendingMachine


def test_huga():
    assert True


def test_insert_10coin():
    vending_machine = VendingMachine()
    coins = 10
    vending_machine.insert(coins)


def test_check_coins():
    vending_machine = VendingMachine()
    insert_coins = 10
    vending_machine.insert(insert_coins)
    actual = vending_machine.coins
    expected = {10: 1, 50: 0, 100: 0, 500: 0, 1000: 0}

    assert actual == expected
