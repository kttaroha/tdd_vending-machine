from vending_machine.hoge.huga import Huga


class TestHuga:
    def test_huga(self):
        assert Huga().piyo() == "piyo"
