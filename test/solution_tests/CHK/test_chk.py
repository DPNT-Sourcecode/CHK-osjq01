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
        assert checkout_solution.checkout("ABAABCABAABABD") == 455

    def test_chkDiscount4(self):
        assert checkout_solution.checkout("ABEE") == 130

    def test_chkDiscount5(self):
        assert checkout_solution.checkout("AEE") == 130

    def test_chkDiscount6(self):
        assert checkout_solution.checkout("AAAAAAAA") == 330

    def test_chkDiscount7(self):
        assert checkout_solution.checkout("AAAAAAAAA") == 380

    def test_chkDiscount8(self):
        assert checkout_solution.checkout("EEEEBB") == 160

    def test_chkDiscount9(self):
        assert checkout_solution.checkout("FF") == 20

    def test_chkDiscount10(self):
        assert checkout_solution.checkout("FFF") == 20

    def test_chkDiscount11(self):
        assert checkout_solution.checkout("FFFFFFF") == 50

    def test_chkWrongProduct(self):
        assert checkout_solution.checkout("a") == -1

    def test_chkWrongProduct2(self):
        assert checkout_solution.checkout("A-C") == -1

