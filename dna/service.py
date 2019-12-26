from dna.simian_analyzer import SimianAnalyzer
from dna.validator import check


class Dna:

    def __init__(self):
        self.simian = SimianAnalyzer()

    def isSimian(self, dna: list) -> bool:
        check(dna)
        return self.simian.analyze(dna)
