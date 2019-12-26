from accessify import private

import constant


class Validator:

    def dna(self, dna: list) -> bool:
        size = len(dna)
        for sequence in dna:
            self.checkSequence(sequence, size)
        return True

    @private
    def checkSequence(self, sequence: str, size: int) -> bool:
        self.isSquare(sequence, size)
        self.isNitrogenousBase(sequence)
        return True

    @private
    def isSquare(self, sequence: str, size: int) -> bool:
        if len(sequence) != size:
            raise Exception("INVALID_DNA_SEQUENCE")
        return True

    @private
    def isNitrogenousBase(self, sequence: str) -> bool:
        if any(letter not in constant.NITROGENOUS_BASE for letter in sequence):
            raise Exception("INVALID_DNA")
        return True
