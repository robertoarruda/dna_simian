import constant


def bySize(dna: list) -> bool:
    if len(dna) < constant.SEQUENCE_SIZE:
        return False
    return True


def splitFields(dna: list, row: int) -> dict:
    return {'f1': dna[row], 'f2': dna[row + 1], 'f3': dna[row + 2], 'f4': dna[row + 3]}


def getSequence(dna: list, row: int, col: int) -> str:
    split = splitFields(dna, row)
    return '{}{}{}{}'.format(split['f1'][col], split['f2'][col], split['f3'][col], split['f4'][col])


def getSequenceByIncrColumns(dna: list, row: int, col: int) -> str:
    split = splitFields(dna, row)
    return '{}{}{}{}'.format(split['f1'][col], split['f2'][col + 1], split['f3'][col + 2], split['f4'][col + 3])


def getSequenceByDecrColumns(dna: list, row: int, col: int) -> str:
    split = splitFields(dna, row)
    return '{}{}{}{}'.format(split['f1'][col], split['f2'][col - 1], split['f3'][col - 2], split['f4'][col - 3])


class SimianAnalyzer:
    simian_sequence_found: int = 0

    def analyze(self, dna: list) -> bool:
        if not bySize(dna):
            return False

        if self.isHorizontalSequence(dna):
            return True

        if self.isVerticalSequence(dna):
            return True

        if self.isDiagonalSequence(dna):
            return True

        if self.isInvertedDiagonalSequence(dna):
            return True

        return False

    def incrementSimianSequence(self) -> int:
        self.simian_sequence_found += 1
        return self.simian_sequence_found

    def checkSequence(self) -> bool:
        if self.simian_sequence_found < constant.SEQUENCE_TIMES:
            return False
        return True

    def isHorizontalSequence(self, dna: list) -> bool:
        for sequence in dna:
            start = 0
            while start <= len(sequence) - constant.SEQUENCE_SIZE:
                if sequence[start:constant.SEQUENCE_SIZE + start] not in constant.SEQUENCE:
                    start += 1
                    continue
                self.incrementSimianSequence()
                start += constant.SEQUENCE_SIZE
                if self.checkSequence():
                    return True
        return False

    def isVerticalSequence(self, dna: list) -> bool:
        for column in range(len(dna[0])):
            row = 0
            while row <= len(dna) - constant.SEQUENCE_SIZE:
                if getSequence(dna, row, column) not in constant.SEQUENCE:
                    row += 1
                    continue
                self.incrementSimianSequence()
                row += constant.SEQUENCE_SIZE
                if self.checkSequence():
                    return True
        return False

    def isDiagonalSequence(self, dna: list) -> bool:
        i_sequence_size = constant.SEQUENCE_SIZE - 1
        for row in range(len(dna) - i_sequence_size):
            column = len(dna[0]) - constant.SEQUENCE_SIZE
            while column >= 0:
                column = column if row == 0 else 0
                diagonal_column = column
                diagonal_row = row
                while diagonal_row < len(dna) - i_sequence_size and diagonal_column < len(dna[0]) - i_sequence_size:
                    if getSequenceByIncrColumns(dna, diagonal_row, diagonal_column) not in constant.SEQUENCE:
                        diagonal_row += 1
                        diagonal_column += 1
                        continue
                    self.incrementSimianSequence()
                    diagonal_row += constant.SEQUENCE_SIZE
                    diagonal_column += constant.SEQUENCE_SIZE
                    if self.checkSequence():
                        return True
                column -= 1
        return False

    def isInvertedDiagonalSequence(self, dna: list) -> bool:
        i_sequence_size = constant.SEQUENCE_SIZE - 1
        for row in range(len(dna) - i_sequence_size):
            column = i_sequence_size
            while column < len(dna[0]):
                column = column if row == 0 else len(dna[0]) - 1
                diagonal_column = column
                diagonal_row = row
                while diagonal_row < len(dna) - i_sequence_size and diagonal_column >= i_sequence_size:
                    if getSequenceByDecrColumns(dna, diagonal_row, diagonal_column) not in constant.SEQUENCE:
                        diagonal_row += 1
                        diagonal_column -= 1
                        continue
                    self.incrementSimianSequence()
                    diagonal_row += constant.SEQUENCE_SIZE
                    diagonal_column -= constant.SEQUENCE_SIZE
                    if self.checkSequence():
                        return True
                column += 1
        return False
