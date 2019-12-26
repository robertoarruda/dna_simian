import unittest

from dna.validator import check, sizeIsCorrect, isNitrogenousBase


class MyTestCase(unittest.TestCase):
    def testCheck(self):
        dna = ["CTGAGA", "CTAACC", "TCACGT", "ATACTT", "CCTTGT", "TCTTTT"]
        self.assertTrue(check(dna))

    def testSizeIsCorrect(self):
        sequence = "CTGAGA"
        size = len(sequence)
        self.assertTrue(sizeIsCorrect(sequence, size))

    def testSizeIsCorrectError(self):
        sequence = "CTGAGA"
        size = len(sequence) + 10
        with self.assertRaises(Exception, msg="INVALID_DNA_SEQUENCE"):
            sizeIsCorrect(sequence, size)

    def testIsNitrogenousBase(self):
        sequence = "CTGAGA"
        self.assertTrue(isNitrogenousBase(sequence))

    def testIsNitrogenousBaseError(self):
        sequence = "PALMEIRAS"
        with self.assertRaises(Exception, msg="INVALID_DNA"):
            isNitrogenousBase(sequence)


if __name__ == '__main__':
    unittest.main()
