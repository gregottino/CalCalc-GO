from unittest import TestCase
import CalCalc


class CalCalcTestCall(TestCase):
    def test_1(self):
        """Test if error is handled for junk without wolfram flag"""
        test_str = "some junk"
        assert (
            CalCalc.calculate(test_str, False)
            == test_str
            + " : is not a valid numexpr expression and cannon be evaluated, try with wolfram alpha '-w' flag"
        )


    def test_2(self):
        """Test if error is handled for junk with wolfram flag"""
        test_str = "what the heck is going on here"
        assert CalCalc.calculate(test_str, True) == "unreadable input by wolfram, please reformat"


    def test_3(self):
        """Test that a simple calculation of 2+2 returns 4"""
        test_str = "2+2"
        assert CalCalc.calculate(test_str, False) == 4.0


    def test_4(self):
        """Check that floating point output works for an answer that returns scientific notation"""
        test_str = "mass of the moon in kg"
        assert CalCalc.get_wolfram_output_as_float(CalCalc.calculate(test_str, True)) == 7.3459e22


    def test_5(self):
        """Check that the floating point output returns results that have a multiplier as string"""
        test_str = "millimeters in a meter"
        assert CalCalc.get_wolfram_output_as_float(CalCalc.calculate(test_str, True)) == 1.0e3
