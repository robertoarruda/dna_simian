from accessify import private

import constant


class SimianAnalyzer:
    simian_sequence_found: int = 0

    def analyze(self, dna: list) -> bool:
        if not self.bySize(dna):
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

    @private
    def incrementSimianSequence(self) -> int:
        self.simian_sequence_found += 1
        return self.simian_sequence_found

    @private
    def checkSequence(self) -> bool:
        if self.simian_sequence_found < constant.SEQUENCE_TIMES:
            return False
        return True

    @private
    def bySize(self, dna: list) -> bool:
        if len(dna) < constant.SEQUENCE_SIZE:
            return False
        return True

    @private
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

    @private
    def splitFields(self, dna: list, row: int) -> dict:
        return {'f1': dna[row], 'f2': dna[row + 1], 'f3': dna[row + 2], 'f4': dna[row + 3]}

    @private
    def getSequence(self, dna: list, row: int, col: int) -> str:
        split = self.splitFields(dna, row)
        return '{}{}{}{}'.format(split['f1'][col], split['f2'][col], split['f3'][col], split['f4'][col])

    @private
    def isVerticalSequence(self, dna: list) -> bool:
        for column in range(len(dna[0])):
            row = 0
            while row <= len(dna) - constant.SEQUENCE_SIZE:
                if self.getSequence(dna, row, column) not in constant.SEQUENCE:
                    row += 1
                    continue
                self.incrementSimianSequence()
                row += constant.SEQUENCE_SIZE
                if self.checkSequence():
                    return True
        return False

    @private
    def getSequenceByIncrColumns(self, dna: list, row: int, col: int) -> str:
        split = self.splitFields(dna, row)
        return '{}{}{}{}'.format(split['f1'][col], split['f2'][col + 1], split['f3'][col + 2], split['f4'][col + 3])

    @private
    def isDiagonalSequence(self, dna: list) -> bool:
        for row in range(len(dna) - (constant.SEQUENCE_SIZE - 1)):
            column = len(dna[0]) - constant.SEQUENCE_SIZE
            while column >= 0:
                column = column if row == 0 else 0
                diagonal_column = column
                diagonal_row = row
                while diagonal_row < len(dna) - (constant.SEQUENCE_SIZE - 1) \
                        and diagonal_column < len(dna[0]) - (constant.SEQUENCE_SIZE - 1):
                    if self.getSequenceByIncrColumns(dna, diagonal_row, diagonal_column) not in constant.SEQUENCE:
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

    @private
    def getSequenceByDecrColumns(self, dna: list, row: int, col: int) -> str:
        split = self.splitFields(dna, row)
        return '{}{}{}{}'.format(split['f1'][col], split['f2'][col - 1], split['f3'][col - 2], split['f4'][col - 3])

    @private
    def isInvertedDiagonalSequence(self, dna: list) -> bool:
        for row in range(len(dna) - (constant.SEQUENCE_SIZE - 1)):
            column = constant.SEQUENCE_SIZE - 1
            while column < len(dna[0]):
                column = column if row == 0 else len(dna[0]) - 1
                diagonal_column = column
                diagonal_row = row
                while diagonal_row < len(dna) - (
                        constant.SEQUENCE_SIZE - 1) and diagonal_column >= constant.SEQUENCE_SIZE - 1:
                    if self.getSequenceByDecrColumns(dna, diagonal_row, diagonal_column) not in constant.SEQUENCE:
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
