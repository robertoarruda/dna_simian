import asyncio
import hashlib
from decimal import Decimal
from typing import List

import boto3
from boto3.dynamodb.conditions import Attr

from dna.simian_analyzer import SimianAnalyzer
from dna.validator import Validator


class Dna:
    def __init__(self):
        self.simian = SimianAnalyzer()
        self.dna_table = boto3.resource("dynamodb").Table("dna")
        self.stats_table = boto3.resource("dynamodb").Table("stats")

    @staticmethod
    def __generateId(dna: List[str]) -> str:
        return hashlib.md5("".join(dna).encode("utf-8")).hexdigest()

    @staticmethod
    def __calcRatio(simians: int, humans: int) -> Decimal:
        if not humans:
            return Decimal(0)
        return Decimal(simians / humans).quantize(Decimal("1.0"))

    async def __generateStats(self) -> dict:
        query = self.dna_table.scan(Select="COUNT", FilterExpression=Attr("is_simian").eq(True))
        simians = query.get("Count", 0)
        humans = query.get("ScannedCount", 0) - simians
        item = {'_id': "1", 'simians': simians, 'humans': humans, 'ratio': self.__calcRatio(simians, humans)}
        self.stats_table.put_item(Item=item)
        return item

    def store(self, dna: List[str]) -> dict:
        Validator.check(dna)
        item = {'_id': self.__generateId(dna), 'dna': dna, 'is_simian': self.isSimian(dna)}
        self.dna_table.put_item(Item=item)
        asyncio.run(self.__generateStats())
        return item

    def isSimian(self, dna: List[str]) -> bool:
        return self.simian.analyze(dna)

    def stats(self) -> dict:
        stats = self.stats_table.scan(Limit=1).get("Items", [])[0]
        return {'count_mutant_dna': str(stats.get("simians")), 'count_human_dna': str(stats.get("humans")),
                'ratio': str(stats.get("ratio"))}
