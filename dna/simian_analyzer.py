import constant


class SimianAnalyzer:
    __simian_sequence_found: int = 0

    def analyze(self, dna: list) -> bool:
        if not self.__bySize(dna):
            return False

        if self.__isHorizontalSequence(dna):
            return True

        if self.__isVerticalSequence(dna):
            return True

        if self.__isDiagonalSequence(dna):
            return True

        if self.__isInvertedDiagonalSequence(dna):
            return True

        return False

    @staticmethod
    def __bySize(dna: list) -> bool:
        if len(dna) < constant.SEQUENCE_SIZE:
            return False
        return True

    @staticmethod
    def __getSequence(dna: list, row: int, col: int) -> str:
        sequence = ""
        for i in range(constant.SEQUENCE_SIZE):
            sequence += dna[row + i][col]
        return sequence

    @staticmethod
    def __getSequenceByIncrColumns(dna: list, row: int, col: int) -> str:
        sequence = ""
        for i in range(constant.SEQUENCE_SIZE):
            sequence += dna[row + i][col + i]
        return sequence

    @staticmethod
    def __getSequenceByDecrColumns(dna: list, row: int, col: int) -> str:
        sequence = ""
        for i in range(constant.SEQUENCE_SIZE):
            sequence += dna[row + i][col - i]
        return sequence

    def __incrementSimianSequence(self) -> int:
        self.__simian_sequence_found += 1
        return self.__simian_sequence_found

    def checkSequence(self) -> bool:
        if self.__simian_sequence_found < constant.SEQUENCE_TIMES:
            return False
        return True

    def __isHorizontalSequence(self, dna: list) -> bool:
        for sequence in dna:
            start = 0
            while start <= len(sequence) - constant.SEQUENCE_SIZE:
                if sequence[start:constant.SEQUENCE_SIZE + start] not in constant.SEQUENCE:
                    start += 1
                    continue
                self.__incrementSimianSequence()
                start += constant.SEQUENCE_SIZE
                if self.checkSequence():
                    return True
        return False

    def __isVerticalSequence(self, dna: list) -> bool:
        for column in range(len(dna[0])):
            row = 0
            while row <= len(dna) - constant.SEQUENCE_SIZE:
                if self.__getSequence(dna, row, column) not in constant.SEQUENCE:
                    row += 1
                    continue
                self.__incrementSimianSequence()
                row += constant.SEQUENCE_SIZE
                if self.checkSequence():
                    return True
        return False

    def __isDiagonalSequence(self, dna: list) -> bool:
        i_sequence_size = constant.SEQUENCE_SIZE - 1
        for row in range(len(dna) - i_sequence_size):
            column = len(dna[0]) - constant.SEQUENCE_SIZE
            while column >= 0:
                column = column if row == 0 else 0
                diagonal_column = column
                diagonal_row = row
                while diagonal_row < len(dna) - i_sequence_size and diagonal_column < len(dna[0]) - i_sequence_size:
                    if self.__getSequenceByIncrColumns(dna, diagonal_row, diagonal_column) not in constant.SEQUENCE:
                        diagonal_row += 1
                        diagonal_column += 1
                        continue
                    self.__incrementSimianSequence()
                    diagonal_row += constant.SEQUENCE_SIZE
                    diagonal_column += constant.SEQUENCE_SIZE
                    if self.checkSequence():
                        return True
                column -= 1
        return False

    def __isInvertedDiagonalSequence(self, dna: list) -> bool:
        i_sequence_size = constant.SEQUENCE_SIZE - 1
        for row in range(len(dna) - i_sequence_size):
            column = i_sequence_size
            while column < len(dna[0]):
                column = column if row == 0 else len(dna[0]) - 1
                diagonal_column = column
                diagonal_row = row
                while diagonal_row < len(dna) - i_sequence_size and diagonal_column >= i_sequence_size:
                    if self.__getSequenceByDecrColumns(dna, diagonal_row, diagonal_column) not in constant.SEQUENCE:
                        diagonal_row += 1
                        diagonal_column -= 1
                        continue
                    self.__incrementSimianSequence()
                    diagonal_row += constant.SEQUENCE_SIZE
                    diagonal_column -= constant.SEQUENCE_SIZE
                    if self.checkSequence():
                        return True
                column += 1
        return False
