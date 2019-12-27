import asyncio
import unittest
from decimal import Decimal
from unittest.mock import MagicMock
from unittest.mock import patch

from dna.service import Dna


class DnaTest(unittest.TestCase):
    @patch("hashlib.md5")
    def testGenerateId(self, hashlib_md5: MagicMock):
        dna = ["CTGAGA", "CTAACC", "TCACGT", "ATACTT", "CCTTGT", "TCTTTT"]
        expected = "XXX-123-HASH-789-XXX"
        hashlib_md5.return_value.hexdigest.return_value = expected
        self.assertEqual(expected, Dna._Dna__generateId(dna))

    def testCalcRatio(self):
        simians = 40
        humans = 100
        expected = Decimal("0.4").quantize(Decimal("1.0"))
        self.assertEqual(expected, Dna._Dna__calcRatio(simians, humans))

    def testCalcRatioZero(self):
        simians = 40
        humans = 0
        expected = Decimal("0").quantize(Decimal("1.0"))
        self.assertEqual(expected, Dna._Dna__calcRatio(simians, humans))

    @patch('boto3.resource')
    def testGenerateStats(self, boto3_resource: MagicMock):
        boto3_resource.return_value.Table.return_value.scan.return_value = {'Count': 40, 'ScannedCount': 140}
        obj = Dna()
        expected = {'_id': "1", 'simians': 40, 'humans': 100, 'ratio': Decimal("0.4")}
        self.assertEqual(expected, asyncio.run(obj._Dna__generateStats()))

    @patch('boto3.resource')
    @patch("dna.service.Validator.check")
    @patch("hashlib.md5")
    @patch("dna.service.SimianAnalyzer.analyze")
    def testStore(self, simian_analyzer: MagicMock, hashlib_md5: MagicMock, validator_check: MagicMock,
                  boto3_resource: MagicMock):
        dna = ["CTGAGA", "CTAACC", "TCACGT", "ATACTT", "CCTTGT", "TCTTTT"]
        validator_check.return_value = True
        boto3_resource.return_value.Table.return_value.put_item.return_value = True
        boto3_resource.return_value.Table.return_value.scan.return_value = {'Count': 40, 'ScannedCount': 140}
        hash_md5 = "XXX-123-HASH-789-XXX"
        hashlib_md5.return_value.hexdigest.return_value = hash_md5
        simian_analyzer.return_value = True
        obj = Dna()
        expected = {'_id': hash_md5, 'is_simian': True}
        self.assertEqual(expected, obj.store(dna))

    @patch("dna.service.SimianAnalyzer.analyze")
    def testIsSimian(self, simian_analyzer: MagicMock):
        dna = ["CTGAGA", "CTAACC", "TCACGT", "ATACTT", "CCTTGT", "TCTTTT"]
        simian_analyzer.return_value = True
        obj = Dna()
        self.assertTrue(obj.isSimian(dna))

    @patch('boto3.resource')
    def testStats(self, boto3_resource: MagicMock):
        simians = "40"
        humans = "100"
        ratio = "0.4"
        boto3_resource.return_value.Table.return_value.scan.return_value = {
            'Items': [{'simians': Decimal(simians), 'humans': Decimal(humans), 'ratio': Decimal(ratio)}]}
        obj = Dna()
        expected = {'count_mutant_dna': simians, 'count_human_dna': humans, 'ratio': ratio}
        self.assertEqual(expected, obj.stats())


if __name__ == '__main__':
    unittest.main()
