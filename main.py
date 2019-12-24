from services import Dna


class Main:

    def __init__(self):
        self.dna = Dna()

    def check(self, dna: object) -> bool:
        return self.dna.isSimian(dna)


main = Main()
res = main.check(["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"])

print(res)
