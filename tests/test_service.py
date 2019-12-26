import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from dna.service import Dna


class MyTestCase(unittest.TestCase):
    @patch("dna.service.SimianAnalyzer.analyze")
    @patch("dna.service.check")
    def testIsSimian(self, validator_check: MagicMock, simian_analyzer: MagicMock):
        dna = ["CTGAGA", "CTAACC", "TCACGT", "ATACTT", "CCTTGT", "TCTTTT"]
        validator_check.return_value = True
        simian_analyzer.return_value = True
        obj = Dna()
        self.assertTrue(obj.isSimian(dna))

    @patch("dna.service.SimianAnalyzer.analyze")
    @patch("dna.service.check")
    def testIsSimianNegative(self, validator_check: MagicMock, simian_analyzer: MagicMock):
        dna = ["CTGAGA", "CTAACC", "TCACGT", "ATACTT", "CCTTGT", "TCTTTT"]
        validator_check.return_value = True
        simian_analyzer.return_value = False
        obj = Dna()
        self.assertFalse(obj.isSimian(dna))


if __name__ == '__main__':
    unittest.main()
