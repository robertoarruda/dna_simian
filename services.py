from accessify import private

import constant


class Dna:

    def __init__(self):
        self.validate = Validate()
        self.simian = Simian()

    def isSimian(self, dna: object) -> bool:
        self.validate.dna(dna)
        return self.simian.check(dna)


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
        if any(letter not in constant.NITROGENOUS_BASE for letter in sequence):
            raise Exception("INVALID_DNA")
        return True


class Simian:
    __sequence = 0

    def check(self, dna: object) -> bool:
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
    def incrementSequence(self) -> int:
        self.__sequence += 1
        return self.__sequence

    @private
    def checkSequence(self) -> bool:
        if self.__sequence < constant.SEQUENCE_TIMES:
            return False
        return True

    @private
    def bySize(self, dna: object) -> bool:
        if len(dna) < constant.SEQUENCE_SIZE:
            return False
        return True

    @private
    def isHorizontalSequence(self, dna: object) -> bool:
        for sequence in dna:
            start = 0
            while start <= len(sequence) - constant.SEQUENCE_SIZE:
                if sequence[start:constant.SEQUENCE_SIZE + start] not in constant.SEQUENCE:
                    start += 1
                    continue
                self.incrementSequence()
                start += constant.SEQUENCE_SIZE
                if self.checkSequence():
                    return True
        return False

    @private
    def isVerticalSequence(self, dna: object) -> bool:
        for column in range(len(dna[0])):
            row = 0
            while row <= len(dna) - constant.SEQUENCE_SIZE:
                field1 = dna[row][column]
                field2 = dna[row + 1][column]
                field3 = dna[row + 2][column]
                field4 = dna[row + 3][column]
                sequence = '{}{}{}{}'.format(field1, field2, field3, field4)
                if sequence not in constant.SEQUENCE:
                    row += 1
                    continue
                self.incrementSequence()
                row += constant.SEQUENCE_SIZE
                if self.checkSequence():
                    return True
        return False

    @private
    def isDiagonalSequence(self, dna: object) -> bool:
        for row in range(len(dna) - (constant.SEQUENCE_SIZE - 1)):
            column = len(dna[0]) - constant.SEQUENCE_SIZE
            while column >= 0:
                column = column if row == 0 else 0
                diagonal_column = column
                diagonal_row = row
                while diagonal_row < len(dna) - (constant.SEQUENCE_SIZE - 1) \
                        and diagonal_column < len(dna[0]) - (constant.SEQUENCE_SIZE - 1):
                    field1 = dna[diagonal_row][diagonal_column]
                    field2 = dna[diagonal_row + 1][diagonal_column + 1]
                    field3 = dna[diagonal_row + 2][diagonal_column + 2]
                    field4 = dna[diagonal_row + 3][diagonal_column + 3]
                    sequence = '{}{}{}{}'.format(field1, field2, field3, field4)
                    if sequence not in constant.SEQUENCE:
                        diagonal_row += 1
                        diagonal_column += 1
                        continue
                    self.incrementSequence()
                    diagonal_row += constant.SEQUENCE_SIZE
                    diagonal_column += constant.SEQUENCE_SIZE
                    if self.checkSequence():
                        return True
                column -= 1
        return False

    @private
    def isInvertedDiagonalSequence(self, dna: object) -> bool:
        for row in range(len(dna) - (constant.SEQUENCE_SIZE - 1)):
            column = constant.SEQUENCE_SIZE - 1
            while column < len(dna[0]):
                column = column if row == 0 else len(dna[0]) - 1
                diagonal_column = column
                diagonal_row = row
                while diagonal_row < len(dna) - (
                        constant.SEQUENCE_SIZE - 1) and diagonal_column >= constant.SEQUENCE_SIZE - 1:
                    field1 = dna[diagonal_row][diagonal_column]
                    field2 = dna[diagonal_row + 1][diagonal_column - 1]
                    field3 = dna[diagonal_row + 2][diagonal_column - 2]
                    field4 = dna[diagonal_row + 3][diagonal_column - 3]
                    sequence = '{}{}{}{}'.format(field1, field2, field3, field4)
                    if sequence not in constant.SEQUENCE:
                        diagonal_row += 1
                        diagonal_column -= 1
                        continue
                    self.incrementSequence()
                    diagonal_row += constant.SEQUENCE_SIZE
                    diagonal_column -= constant.SEQUENCE_SIZE
                    if self.checkSequence():
                        return True
                column += 1
        return False
