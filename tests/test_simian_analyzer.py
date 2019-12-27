import unittest
from unittest.mock import patch

from dna.simian_analyzer import SimianAnalyzer


class SimianAnalyzerTest(unittest.TestCase):
    @patch("constant.SEQUENCE_TIMES", 1)
    @patch("constant.SEQUENCE_SIZE", 4)
    def testAnalyzeIsHorizontalSequence(self):
        dna = [
            "------",
            "------",
            "------",
            "------",
            "------",
            "--TTTT"]
        obj = SimianAnalyzer()
        self.assertTrue(obj.analyze(dna))

    @patch("constant.SEQUENCE_TIMES", 1)
    @patch("constant.SEQUENCE_SIZE", 4)
    def testAnalyzeIsVerticalSequence(self):
        dna = [
            "------",
            "------",
            "-----T",
            "-----T",
            "-----T",
            "-----T"]
        obj = SimianAnalyzer()
        self.assertTrue(obj.analyze(dna))

    @patch("constant.SEQUENCE_TIMES", 1)
    @patch("constant.SEQUENCE_SIZE", 4)
    def testAnalyzeIsDiagonalSequence(self):
        dna = [
            "------",
            "------",
            "T-----",
            "-T----",
            "--T---",
            "---T--"]
        obj = SimianAnalyzer()
        self.assertTrue(obj.analyze(dna))

    @patch("constant.SEQUENCE_TIMES", 1)
    @patch("constant.SEQUENCE_SIZE", 4)
    def testAnalyzeIsInvertedDiagonalSequence(self):
        dna = [
            "------",
            "------",
            "-----T",
            "----T-",
            "---T--",
            "--T---"]
        obj = SimianAnalyzer()
        self.assertTrue(obj.analyze(dna))

    def testAnalyzeFalse(self):
        dna = [
            "------",
            "------",
            "------",
            "------",
            "------",
            "------"]
        obj = SimianAnalyzer()
        self.assertFalse(obj.analyze(dna))

    def testAnalyzeFalseBySize(self):
        dna = ["CTGAGA"]
        obj = SimianAnalyzer()
        self.assertFalse(obj.analyze(dna))

    def testBySize(self):
        dna = ["CTGAGA", "CTAACC", "TCACGT", "ATACTT", "CCTTGT", "TCTTTT"]
        self.assertTrue(SimianAnalyzer._SimianAnalyzer__bySize(dna))

    def testBySizeFalse(self):
        dna = ["CTGAGA"]
        self.assertFalse(SimianAnalyzer._SimianAnalyzer__bySize(dna))

    def testGetSequence(self):
        dna = ["CTGAGA", "CTAACC", "TCACGT", "ATACTT", "CCTTGT", "TCTTTT"]
        row = 0
        col = 0
        expected = '{}{}{}{}'.format(dna[row][col], dna[row + 1][col], dna[row + 2][col], dna[row + 3][col])
        self.assertEqual(expected, SimianAnalyzer._SimianAnalyzer__getSequence(dna, row, col))

    def testGetSequenceByIncrColumns(self):
        dna = ["CTGAGA", "CTAACC", "TCACGT", "ATACTT", "CCTTGT", "TCTTTT"]
        row = 0
        col = 0
        expected = '{}{}{}{}'.format(dna[row][col], dna[row + 1][col + 1], dna[row + 2][col + 2], dna[row + 3][col + 3])
        self.assertEqual(expected, SimianAnalyzer._SimianAnalyzer__getSequenceByIncrColumns(dna, row, col))

    def testGetSequenceByDecrColumns(self):
        dna = ["CTGAGA", "CTAACC", "TCACGT", "ATACTT", "CCTTGT", "TCTTTT"]
        row = 0
        col = 5
        expected = '{}{}{}{}'.format(dna[row][col], dna[row + 1][col - 1], dna[row + 2][col - 2], dna[row + 3][col - 3])
        self.assertEqual(expected, SimianAnalyzer._SimianAnalyzer__getSequenceByDecrColumns(dna, row, col))

    def testIncrementSimianSequence(self):
        obj = SimianAnalyzer()
        self.assertEqual(0, obj._SimianAnalyzer__simian_sequence_found)
        self.assertEqual(1, obj._SimianAnalyzer__incrementSimianSequence())
        self.assertEqual(1, obj._SimianAnalyzer__simian_sequence_found)

    @patch("constant.SEQUENCE_TIMES", 10)
    def testCheckSequence(self):
        obj = SimianAnalyzer()
        obj._SimianAnalyzer__simian_sequence_found = 10
        self.assertTrue(obj.checkSequence())

    @patch("constant.SEQUENCE_TIMES", 20)
    def testCheckSequenceFalse(self):
        obj = SimianAnalyzer()
        obj._SimianAnalyzer__simian_sequence_found = 10
        self.assertFalse(obj.checkSequence())

    @patch("constant.SEQUENCE_TIMES", 1)
    @patch("constant.SEQUENCE_SIZE", 4)
    def testIsHorizontalSequence(self):
        dna = [
            "------",
            "------",
            "------",
            "------",
            "------",
            "--TTTT"]
        obj = SimianAnalyzer()
        obj._SimianAnalyzer__simian_sequence_found = 0
        self.assertTrue(obj._SimianAnalyzer__isHorizontalSequence(dna))

    @patch("constant.SEQUENCE_TIMES", 2)
    @patch("constant.SEQUENCE_SIZE", 4)
    def testIsHorizontalSequenceSkip(self):
        dna = [
            "---------",
            "---------",
            "---------",
            "---------",
            "---------",
            "---------",
            "---------",
            "---------",
            "--TTTTTTT"]
        obj = SimianAnalyzer()
        obj._SimianAnalyzer__simian_sequence_found = 0
        self.assertFalse(obj._SimianAnalyzer__isHorizontalSequence(dna))

    @patch("constant.SEQUENCE_TIMES", 2)
    @patch("constant.SEQUENCE_SIZE", 4)
    def testIsHorizontalSequenceMultiple(self):
        dna = [
            "---------",
            "---------",
            "---------",
            "---------",
            "---------",
            "---------",
            "---------",
            "---------",
            "-TTTTAAAA"]
        obj = SimianAnalyzer()
        obj._SimianAnalyzer__simian_sequence_found = 0
        self.assertTrue(obj._SimianAnalyzer__isHorizontalSequence(dna))

    @patch("constant.SEQUENCE_TIMES", 2)
    @patch("constant.SEQUENCE_SIZE", 4)
    def testIsHorizontalSequenceMultipleSplitted(self):
        dna = [
            "---------",
            "---------",
            "---------",
            "---------",
            "---------",
            "---------",
            "---------",
            "---------",
            "TTTT-AAAA"]
        obj = SimianAnalyzer()
        obj._SimianAnalyzer__simian_sequence_found = 0
        self.assertTrue(obj._SimianAnalyzer__isHorizontalSequence(dna))

    @patch("constant.SEQUENCE_TIMES", 3)
    @patch("constant.SEQUENCE_SIZE", 4)
    def testIsHorizontalSequenceMultipleRows(self):
        dna = [
            "--AAAA",
            "------",
            "------",
            "------",
            "------",
            "--TTTT"]
        obj = SimianAnalyzer()
        obj._SimianAnalyzer__simian_sequence_found = 1
        self.assertTrue(obj._SimianAnalyzer__isHorizontalSequence(dna))

    @patch("constant.SEQUENCE_TIMES", 1)
    @patch("constant.SEQUENCE_SIZE", 4)
    def testIsVerticalSequence(self):
        dna = [
            "------",
            "------",
            "-----T",
            "-----T",
            "-----T",
            "-----T"]
        obj = SimianAnalyzer()
        obj._SimianAnalyzer__simian_sequence_found = 0
        self.assertTrue(obj._SimianAnalyzer__isVerticalSequence(dna))

    @patch("constant.SEQUENCE_TIMES", 2)
    @patch("constant.SEQUENCE_SIZE", 4)
    def testIsVerticalSequenceSkip(self):
        dna = [
            "---------",
            "---------",
            "--------T",
            "--------T",
            "--------T",
            "--------T",
            "--------T",
            "--------T",
            "--------T"]
        obj = SimianAnalyzer()
        obj._SimianAnalyzer__simian_sequence_found = 0
        self.assertFalse(obj._SimianAnalyzer__isVerticalSequence(dna))

    @patch("constant.SEQUENCE_TIMES", 2)
    @patch("constant.SEQUENCE_SIZE", 4)
    def testIsVerticalSequenceMultiple(self):
        dna = [
            "---------",
            "--------T",
            "--------T",
            "--------T",
            "--------T",
            "--------A",
            "--------A",
            "--------A",
            "--------A"]
        obj = SimianAnalyzer()
        obj._SimianAnalyzer__simian_sequence_found = 0
        self.assertTrue(obj._SimianAnalyzer__isVerticalSequence(dna))

    @patch("constant.SEQUENCE_TIMES", 2)
    @patch("constant.SEQUENCE_SIZE", 4)
    def testIsVerticalSequenceMultipleSplitted(self):
        dna = [
            "--------T",
            "--------T",
            "--------T",
            "--------T",
            "---------",
            "--------A",
            "--------A",
            "--------A",
            "--------A"]
        obj = SimianAnalyzer()
        obj._SimianAnalyzer__simian_sequence_found = 0
        self.assertTrue(obj._SimianAnalyzer__isVerticalSequence(dna))

    @patch("constant.SEQUENCE_TIMES", 3)
    @patch("constant.SEQUENCE_SIZE", 4)
    def testIsVerticalSequenceMultipleRows(self):
        dna = [
            "A-----",
            "A-----",
            "A----T",
            "A----T",
            "-----T",
            "-----T"]
        obj = SimianAnalyzer()
        obj._SimianAnalyzer__simian_sequence_found = 1
        self.assertTrue(obj._SimianAnalyzer__isVerticalSequence(dna))

    @patch("constant.SEQUENCE_TIMES", 1)
    @patch("constant.SEQUENCE_SIZE", 4)
    def testIsDiagonalSequence(self):
        dna = [
            "------",
            "------",
            "T-----",
            "-T----",
            "--T---",
            "---T--"]
        obj = SimianAnalyzer()
        obj._SimianAnalyzer__simian_sequence_found = 0
        self.assertTrue(obj._SimianAnalyzer__isDiagonalSequence(dna))

    @patch("constant.SEQUENCE_TIMES", 2)
    @patch("constant.SEQUENCE_SIZE", 4)
    def testIsDiagonalSequenceSkip(self):
        dna = [
            "---------",
            "---------",
            "--T------",
            "---T-----",
            "----T----",
            "-----T---",
            "------T--",
            "-------T-",
            "--------T"]
        obj = SimianAnalyzer()
        obj._SimianAnalyzer__simian_sequence_found = 0
        self.assertFalse(obj._SimianAnalyzer__isDiagonalSequence(dna))

    @patch("constant.SEQUENCE_TIMES", 2)
    @patch("constant.SEQUENCE_SIZE", 4)
    def testIsDiagonalSequenceMultiple(self):
        dna = [
            "---------",
            "-T-------",
            "--T------",
            "---T-----",
            "----T----",
            "-----A---",
            "------A--",
            "-------A-",
            "--------A"]
        obj = SimianAnalyzer()
        obj._SimianAnalyzer__simian_sequence_found = 0
        self.assertTrue(obj._SimianAnalyzer__isDiagonalSequence(dna))

    @patch("constant.SEQUENCE_TIMES", 2)
    @patch("constant.SEQUENCE_SIZE", 4)
    def testIsDiagonalSequenceMultipleSplitted(self):
        dna = [
            "T--------",
            "-T-------",
            "--T------",
            "---T-----",
            "---------",
            "-----A---",
            "------A--",
            "-------A-",
            "--------A"]
        obj = SimianAnalyzer()
        obj._SimianAnalyzer__simian_sequence_found = 0
        self.assertTrue(obj._SimianAnalyzer__isDiagonalSequence(dna))

    @patch("constant.SEQUENCE_TIMES", 3)
    @patch("constant.SEQUENCE_SIZE", 4)
    def testIsDiagonalSequenceMultipleRows(self):
        dna = [
            "--A---",
            "---A--",
            "T---A-",
            "-T---A",
            "--T---",
            "---T--"]
        obj = SimianAnalyzer()
        obj._SimianAnalyzer__simian_sequence_found = 1
        self.assertTrue(obj._SimianAnalyzer__isDiagonalSequence(dna))

    @patch("constant.SEQUENCE_TIMES", 1)
    @patch("constant.SEQUENCE_SIZE", 4)
    def testIsInvertedDiagonalSequence(self):
        dna = [
            "------",
            "------",
            "-----T",
            "----T-",
            "---T--",
            "--T---"]
        obj = SimianAnalyzer()
        obj._SimianAnalyzer__simian_sequence_found = 0
        self.assertTrue(obj._SimianAnalyzer__isInvertedDiagonalSequence(dna))

    @patch("constant.SEQUENCE_TIMES", 2)
    @patch("constant.SEQUENCE_SIZE", 4)
    def testIsInvertedDiagonalSequenceSkip(self):
        dna = [
            "---------",
            "---------",
            "------T--",
            "-----T---",
            "----T----",
            "---T-----",
            "--T------",
            "-T-------",
            "T--------"]
        obj = SimianAnalyzer()
        obj._SimianAnalyzer__simian_sequence_found = 0
        self.assertFalse(obj._SimianAnalyzer__isInvertedDiagonalSequence(dna))

    @patch("constant.SEQUENCE_TIMES", 2)
    @patch("constant.SEQUENCE_SIZE", 4)
    def testIsInvertedDiagonalSequenceMultiple(self):
        dna = [
            "---------",
            "-------T-",
            "------T--",
            "-----T---",
            "----T----",
            "---A-----",
            "--A------",
            "-A-------",
            "A--------"]
        obj = SimianAnalyzer()
        obj._SimianAnalyzer__simian_sequence_found = 0
        self.assertTrue(obj._SimianAnalyzer__isInvertedDiagonalSequence(dna))

    @patch("constant.SEQUENCE_TIMES", 2)
    @patch("constant.SEQUENCE_SIZE", 4)
    def testIsInvertedDiagonalSequenceMultipleSplitted(self):
        dna = [
            "--------T",
            "-------T-",
            "------T--",
            "-----T---",
            "---------",
            "---A-----",
            "--A------",
            "-A-------",
            "A--------"]
        obj = SimianAnalyzer()
        obj._SimianAnalyzer__simian_sequence_found = 0
        self.assertTrue(obj._SimianAnalyzer__isInvertedDiagonalSequence(dna))

    @patch("constant.SEQUENCE_TIMES", 3)
    @patch("constant.SEQUENCE_SIZE", 4)
    def testIsInvertedDiagonalSequenceMultipleRows(self):
        dna = [
            "---A--",
            "--A---",
            "-A---T",
            "A---T-",
            "---T--",
            "--T---"]
        obj = SimianAnalyzer()
        obj._SimianAnalyzer__simian_sequence_found = 1
        self.assertTrue(obj._SimianAnalyzer__isInvertedDiagonalSequence(dna))


if __name__ == '__main__':
    unittest.main()
