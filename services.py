from accessify import private


class Dna:

    def __init__(self):
        self.validate = Validate()
        self.simian = Simian()

    def isSimian(self, dna: object) -> bool:
        self.validate.dna(dna)
        return True


class Validate:

    def dna(self, dna: object) -> bool:
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
        nitrogenous_base = ["A", "T", "C", "G"]
        if any(letter not in nitrogenous_base for letter in sequence):
            raise Exception("INVALID_DNA")
        return True


class Simian:

    pass
