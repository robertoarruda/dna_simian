from dna.simian_analyzer import SimianAnalyzer
from dna.validator import Validator


class Dna:

    def __init__(self):
        self.validator = Validator()
        self.simian = SimianAnalyzer()

    def isSimian(self, dna: list) -> bool:
        self.validator.dna(dna)
        return self.simian.analyze(dna)
