import os

from util import get_seq, is_protein, CODONS_PER_AMINO_ACID

DATA_FILE = os.path.join("../data", "rosalind_mrna.txt")


def get_number_different_rna_strings(seq: str) -> int:
    if not is_protein(seq):
        raise ValueError("sequence is not a DNA string")

    total = 3  # 3 different stop codon possibilities, which are not present in protein string
    for aa in seq:
        total *= CODONS_PER_AMINO_ACID[aa]
    return total % 1000000


def main():
    seqs = get_seq(DATA_FILE)
    number_different_rna_strings = get_number_different_rna_strings(seqs[0])
    print(number_different_rna_strings)


if __name__ == "__main__":
    main()
