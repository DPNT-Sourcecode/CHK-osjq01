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
        assert checkout_solution.checkout("K") == 70

    def test_chkStep4Kb(self):
        assert checkout_solution.checkout("KK") == 120

    def test_chkStep4L(self):
        assert checkout_solution.checkout("L") == 90
        
    def test_chkStep4M(self):
        assert checkout_solution.checkout("M") == 15

    def test_chkStep4Na(self):
        assert checkout_solution.checkout("N") == 40

    def test_chkStep4Nb(self):
        assert checkout_solution.checkout("NNNM") == 120

    def test_chkStep4O(self):
        assert checkout_solution.checkout("O") == 10
        
    def test_chkStep4Pa(self):
        assert checkout_solution.checkout("P") == 50

    def test_chkStep4Pb(self):
        assert checkout_solution.checkout("PPPPP") == 200

    def test_chkStep4Qa(self):
        assert checkout_solution.checkout("Q") == 30
        
    def test_chkStep4Qb(self):
        assert checkout_solution.checkout("QQQ") == 80
        
    def test_chkStep4Ra(self):
        assert checkout_solution.checkout("R") == 50

    def test_chkStep4Rb(self):
        assert checkout_solution.checkout("RRRQ") == 150
        
    def test_chkStep4S(self):
        assert checkout_solution.checkout("S") == 20

    def test_chkStep4T(self):
        assert checkout_solution.checkout("T") == 20
        
    def test_chkStep4Ua(self):
        assert checkout_solution.checkout("U") == 40

    def test_chkStep4Ub(self):
        assert checkout_solution.checkout("UUUU") == 120

    def test_chkStep4Va(self):
        assert checkout_solution.checkout("V") == 50
        
    def test_chkStep4Vb(self):
        assert checkout_solution.checkout("VV") == 90
        
    def test_chkStep4Vc(self):
        assert checkout_solution.checkout("VVV") == 130
        
    def test_chkStep4Vd(self):
        assert checkout_solution.checkout("VVVVV") == 220

    def test_chkStep4W(self):
        assert checkout_solution.checkout("W") == 20

    def test_chkStep4X(self):
        assert checkout_solution.checkout("X") == 17
        
    def test_chkStep4Y(self):
        assert checkout_solution.checkout("Y") == 20
        
    def test_chkStep4Z(self):
        assert checkout_solution.checkout("Z") == 21

    def test_chkAnythree1(self):
        assert checkout_solution.checkout("SSS") == 45

    def test_chkAnythree1(self):
        assert checkout_solution.checkout("STX") == 45

    def test_chkAnythree2(self):
        assert checkout_solution.checkout("SSTTTXZ") == 110

    def test_chkAnythree3(self):
        assert checkout_solution.checkout("STXS") == 62

    def test_chkAnythree4(self):
        assert checkout_solution.checkout("STXZ") == 62

    def test_chkAnythree5(self):
        assert checkout_solution.checkout("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ") == 1602



