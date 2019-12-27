from typing import List

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
