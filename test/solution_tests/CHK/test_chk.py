from lib.solutions.CHK import checkout_solution


class TestChk():
    def test_chkOne(self):
        assert checkout_solution.checkout("A") == 50
