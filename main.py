from dna.service import Dna


class Main:

    def __init__(self):
        self.dna = Dna()

    def check(self, dna: list) -> bool:
        return self.dna.isSimian(dna)


main = Main()
res = main.check(["CTGAGA", "CTAACC", "TCACGT", "ATACTT", "CCTTGT", "TCTTTT"])

# C  T  G  A  G  A
# C  T  A  A  C  C
# T  C  A  C  G  T
# A  T  A  C  T  T
# C  C  T  T  G  T
# T  C  T  T  T  T

print(res)
