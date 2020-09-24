from vending_machine.vending_machine import VendingMachine


def test_huga():
    assert True


def test_insert_10coin():
    vending_machine = VendingMachine()
    coins = 10
    vending_machine.insert(coins)
