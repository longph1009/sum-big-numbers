import unittest
from core import MyBigNumber


class TestCore(unittest.TestCase):
    def setUp(self):
        self.bigNumber = MyBigNumber()

    def test_sum_positive_integers(self):
        self.assertEqual(self.bigNumber.sum("10", "5"), "15")
        self.assertEqual(self.bigNumber.sum("100", "200"), "300")
        self.assertEqual(self.bigNumber.sum("99", "1"), "100")

        long_num1 = "123456789012345678901234567890"
        long_num2 = "987654321098765432109876543210"
        expected_sum = "1111111110111111111011111111100"
        self.assertEqual(self.bigNumber.sum(long_num1, long_num2), expected_sum)

        long_num1 = "999999999999999999999999999999"
        long_num2 = "1"
        expected_sum = "1000000000000000000000000000000"
        self.assertEqual(self.bigNumber.sum(long_num1, long_num2), expected_sum)

    def test_sum_negative_integers(self):
        self.assertEqual(self.bigNumber.sum("-10", "-5"), "-15")
        self.assertEqual(self.bigNumber.sum("-10", "5"), "-5")
        self.assertEqual(self.bigNumber.sum("10", "-5"), "5")
        self.assertEqual(self.bigNumber.sum("-1234567890", "-9876543210"), "-11111111100")
        self.assertEqual(self.bigNumber.sum("-1000000000", "999999999"), "-1")
        self.assertEqual(self.bigNumber.sum("999999999", "-1000000000"), "-1")
        self.assertEqual(self.bigNumber.sum("-50", "100"), "50")
        self.assertEqual(self.bigNumber.sum("100", "-50"), "50")
        self.assertEqual(self.bigNumber.sum("-123", "45"), "-78")
        self.assertEqual(self.bigNumber.sum("45", "-123"), "-78")

    def test_sum_with_zero(self):
        self.assertEqual(self.bigNumber.sum("10", "0"), "10")
        self.assertEqual(self.bigNumber.sum("0", "5"), "5")
        self.assertEqual(self.bigNumber.sum("0", "0"), "0")
        self.assertEqual(self.bigNumber.sum("-0", "0"), "0")

    def test_sum_positive_decimals(self):
        self.assertEqual(self.bigNumber.sum("1.5", "2.5"), "4")
        self.assertEqual(self.bigNumber.sum("1,5", "2,5"), "4")
        self.assertEqual(self.bigNumber.sum("0.1", "0.2"), "0.3")
        self.assertEqual(self.bigNumber.sum("1.99", "0.01"), "2")
        self.assertEqual(self.bigNumber.sum("1.234", "5.6"), "6.834")
        self.assertEqual(self.bigNumber.sum("0.0001", "1,2"), "1.2001")
        self.assertEqual(self.bigNumber.sum("10.5", "0.00567"), "10.50567")
        self.assertEqual(self.bigNumber.sum("3.14159", "2,71"), "5.85159")
        self.assertEqual(self.bigNumber.sum("1.0", "2.00001"), "3.00001")
        self.assertEqual(self.bigNumber.sum("123456789.123456789", "987654321.987654321"), "1111111111.11111111")
        self.assertEqual(self.bigNumber.sum("999999999.999999999", "0.000000001"), "1000000000")
        self.assertEqual(self.bigNumber.sum("0.0000000001", "0.0000000002"), "0.0000000003")
        self.assertEqual(self.bigNumber.sum(".1", ".2"), "0.3")

    def test_sum_negative_decimals(self):
        self.assertEqual(self.bigNumber.sum("-1.5", "-2.5"), "-4")
        self.assertEqual(self.bigNumber.sum("-1.5", "2.0"), "0.5")
        self.assertEqual(self.bigNumber.sum("1.0", "-2.5"), "-1.5")
        self.assertEqual(self.bigNumber.sum("-1.234", "-5.6"), "-6.834")
        self.assertEqual(self.bigNumber.sum("-0.0001", "-1.2"), "-1.2001")
        self.assertEqual(self.bigNumber.sum("-10.5", "-0.00567"), "-10.50567")
        self.assertEqual(self.bigNumber.sum("-3.14159", "-2.71"), "-5.85159")
        self.assertEqual(self.bigNumber.sum("-1.0", "-2.00001"), "-3.00001")
        self.assertEqual(self.bigNumber.sum("-123456789.123456789", "-987654321.987654321"), "-1111111111.11111111")
        self.assertEqual(self.bigNumber.sum("-10.5", "10.5"), "0")
        self.assertEqual(self.bigNumber.sum("0.001", "-0.002"), "-0.001")
        self.assertEqual(self.bigNumber.sum("-0.999", "1.0"), "0.001")

    def test_sum_integer_and_decimal(self):
        self.assertEqual(self.bigNumber.sum("10", "2.5"), "12.5")
        self.assertEqual(self.bigNumber.sum("3.14", "5"), "8.14")
        self.assertEqual(self.bigNumber.sum("7", "0.5"), "7.5")

    def test_sum_leading_zeros(self):
        self.assertEqual(self.bigNumber.sum("010", "005"), "15")
        self.assertEqual(self.bigNumber.sum("0.5", "01.0"), "1.5")


    def test_multiple_commas(self):
        with self.assertRaises(ValueError) as context:
            self.bigNumber.sum("12,34,5", "5")
        self.assertEqual(str(context.exception), "The number has more than one comma")

        with self.assertRaises(ValueError) as context:
            self.bigNumber.sum("123.2,4", "3")
        self.assertEqual(str(context.exception), "The number has more than one comma")

        with self.assertRaises(ValueError) as context:
            self.bigNumber.sum("123.2.4", "3")
        self.assertEqual(str(context.exception), "The number has more than one comma")

        with self.assertRaises(ValueError) as context:
            self.bigNumber.sum("123,2234423.44", "3")
        self.assertEqual(str(context.exception), "The number has more than one comma")

    
    def test_invalid_characters(self):
        with self.assertRaises(ValueError) as context:
            self.bigNumber.sum("123a", "3")
        self.assertEqual(str(context.exception), "The number has invalid character")

        with self.assertRaises(ValueError) as context:
            self.bigNumber.sum("123,2a", "3")
        self.assertEqual(str(context.exception), "The number has invalid character")

        with self.assertRaises(ValueError) as context:
            self.bigNumber.sum("123.2a", "3")
        self.assertEqual(str(context.exception), "The number has invalid character")

        with self.assertRaises(ValueError) as context:
            self.bigNumber.sum("123.2a", "3")
        self.assertEqual(str(context.exception), "The number has invalid character")


if __name__ == '__main__':
    unittest.main()