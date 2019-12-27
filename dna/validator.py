from typing import List

from flask import json

import constant


class Validator:
    @classmethod
    def check(cls, dna: List[str]) -> bool:
        size = len(dna)
        cls.isEmpty(size)
        for sequence in dna:
            cls.sizeIsCorrect(sequence, size)
            cls.isNitrogenousBase(sequence)
        return True

    @staticmethod
    def isEmpty(size: int) -> bool:
        if not size:
            raise Exception("INVALID_DNA")
        return True

    @staticmethod
    def sizeIsCorrect(sequence: str, size: int) -> bool:
        if len(sequence) != size:
            raise Exception("INVALID_DNA_SEQUENCE")
        return True

    @staticmethod
    def isNitrogenousBase(sequence: str) -> bool:
        if any(letter not in constant.NITROGENOUS_BASE for letter in sequence):
            raise Exception("INVALID_DNA")
        return True

    @staticmethod
    def request(data) -> bool:
        try:
            dna = json.loads(data).get("dna", [])
        except Exception as exc:
            raise Exception("INVALID_REQUEST_DATA")
        if not isinstance(dna, List):
            raise Exception("INVALID_DNA")
        if not isinstance(dna[0], str):
            raise Exception("INVALID_DNA_SEQUENCE")
        return True
