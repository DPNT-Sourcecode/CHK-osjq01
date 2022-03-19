from lib.solutions.CHK import checkout_solution


class TestChk():
    def test_chkNone(self):
        assert checkout_solution.checkout("") == 0

    def test_chkOne(self):
        assert checkout_solution.checkout("A") == 50

    def test_chkSome(self):
        assert checkout_solution.checkout("AB") == 80

    def test_chkNoDiscount(self):
        assert checkout_solution.checkout("ABA") == 130

    def test_chkDiscount(self):
        assert checkout_solution.checkout("ABAA") == 160
    


