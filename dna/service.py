from dna.simian_analyzer import SimianAnalyzer
from dna.validator import Validator


class Dna:

    def __init__(self):
        self.simian = SimianAnalyzer()

    def isSimian(self, dna: list) -> bool:
        Validator.check(dna)
        return self.simian.analyze(dna)
