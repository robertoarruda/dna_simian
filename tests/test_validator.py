import unittest

from dna.validator import Validator


class ValidatorTest(unittest.TestCase):
    def testCheck(self):
        dna = ["CTGAGA", "CTAACC", "TCACGT", "ATACTT", "CCTTGT", "TCTTTT"]
        self.assertTrue(Validator.check(dna))

    def testIsEmpty(self):
        dna = ["CTGAGA", "CTAACC", "TCACGT", "ATACTT", "CCTTGT", "TCTTTT"]
        size = len(dna)
        self.assertTrue(Validator.isEmpty(size))

    def testIsEmptyError(self):
        dna = []
        size = len(dna)
        with self.assertRaises(Exception, msg="INVALID_DNA"):
            Validator.isEmpty(size)

    def testSizeIsCorrect(self):
        sequence = "CTGAGA"
        size = len(sequence)
        self.assertTrue(Validator.sizeIsCorrect(sequence, size))

    def testSizeIsCorrectError(self):
        sequence = "CTGAGA"
        size = len(sequence) + 10
        with self.assertRaises(Exception, msg="INVALID_DNA_SEQUENCE"):
            Validator.sizeIsCorrect(sequence, size)

    def testIsNitrogenousBase(self):
        sequence = "CTGAGA"
        self.assertTrue(Validator.isNitrogenousBase(sequence))

    def testIsNitrogenousBaseError(self):
        sequence = "PALMEIRAS"
        with self.assertRaises(Exception, msg="INVALID_DNA"):
            Validator.isNitrogenousBase(sequence)

    def testIsNitrogenousBaseError2(self):
        sequence = "CTGAGa"
        with self.assertRaises(Exception, msg="INVALID_DNA"):
            Validator.isNitrogenousBase(sequence)

    def testRequest(self):
        data = '{"dna": ["CTGAGA", "CTAACC", "TCACGT", "ATACTT", "CCTTGT", "TCTTTT"]}'
        self.assertTrue(Validator.request(data))

    def testRequestInvalid(self):
        data = '{"dna": ["CTGAGA"'
        with self.assertRaises(Exception, msg="INVALID_REQUEST_DATA"):
            Validator.request(data)

    def testRequestEmpty(self):
        data = None
        with self.assertRaises(Exception, msg="INVALID_REQUEST_DATA"):
            Validator.request(data)

    def testRequestInvalidDna(self):
        data = '{"dna": "A"}'
        with self.assertRaises(Exception, msg="INVALID_DNA"):
            Validator.request(data)

    def testRequestInvalidDnaSequence(self):
        data = '{"dna": [0]}'
        with self.assertRaises(Exception, msg="INVALID_DNA_SEQUENCE"):
            Validator.request(data)


if __name__ == '__main__':
    unittest.main()
