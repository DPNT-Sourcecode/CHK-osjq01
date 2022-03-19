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
    
    def test_chkDiscount2(self):
        assert checkout_solution.checkout("ABAABC") == 195
    
    def test_chkDiscount3(self):
        assert checkout_solution.checkout("ABAABCABAABABD") == 465

    def test_chkWrongProduct(self):
        assert checkout_solution.checkout("a") == -1

    def test_chkWrongProduct2(self):
        assert checkout_solution.checkout("A-C") == -1

