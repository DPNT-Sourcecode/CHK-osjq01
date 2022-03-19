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

    def test_chkDiscount11(self):
        assert checkout_solution.checkout("FFFFFFF") == 50

    def test_chkWrongProduct(self):
        assert checkout_solution.checkout("a") == -1

    def test_chkWrongProduct2(self):
        assert checkout_solution.checkout("A-C") == -1
    
    def test_chkStep4G(self):
        assert checkout_solution.checkout("G") == 20

    def test_chkStep4Ha(self):
        assert checkout_solution.checkout("H") == 10

    def test_chkStep4Hb(self):
        assert checkout_solution.checkout("HHHHH") == 45

    def test_chkStep4Hc(self):
        assert checkout_solution.checkout("HHHHHHHHHH") == 80

    def test_chkStep4Hd(self):
        assert checkout_solution.checkout("HHHHHHHHHHHHHHH") == 125

    def test_chkStep4I(self):
        assert checkout_solution.checkout("I") == 35

    def test_chkStep4J(self):
        assert checkout_solution.checkout("J") == 60

    def test_chkStep4Ka(self):
        assert checkout_solution.checkout("K") == 80

    def test_chkStep4Kb(self):
        assert checkout_solution.checkout("KK") == 150

    def test_chkStep4L(self):
        assert checkout_solution.checkout("L") == 90
        
    def test_chkStep4M(self):
        assert checkout_solution.checkout("M") == 15

    def test_chkStep4L(self):
        assert checkout_solution.checkout("L") == 90