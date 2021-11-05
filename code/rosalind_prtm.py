import os

from util import get_seq, is_protein, MONOISOTOPIC_MASS_TABLE

DATA_FILE = os.path.join("../data", "rosalind_prtm.txt")


def get_monoisotopic_mass(seq: str) -> float:
    if not is_protein(seq):
        raise ValueError("sequence is not a protein string")

    mass = 0
    for aa in seq:
        mass += MONOISOTOPIC_MASS_TABLE[aa]
    return mass


def main():
    seqs = get_seq(DATA_FILE)
    mass = get_monoisotopic_mass(seqs[0])
    print(round(mass, 3))


if __name__ == "__main__":
    main()
