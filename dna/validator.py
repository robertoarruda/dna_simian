import constant


def check(dna: list) -> bool:
    size = len(dna)
    for sequence in dna:
        sizeIsCorrect(sequence, size)
        isNitrogenousBase(sequence)
    return True


def sizeIsCorrect(sequence: str, size: int) -> bool:
    if len(sequence) != size:
        raise Exception("INVALID_DNA_SEQUENCE")
    return True


def isNitrogenousBase(sequence: str) -> bool:
    if any(letter not in constant.NITROGENOUS_BASE for letter in sequence):
        raise Exception("INVALID_DNA")
    return True
