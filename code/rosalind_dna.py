import os

from util import get_seq, is_dna

DATA_FILE = os.path.join("../data", "rosalind_dna.txt")


def count_dna_nucleotides(seq: str) -> tuple[int, int, int, int]:
    if not is_dna(seq):
        raise ValueError("sequence is not a DNA string")

    return seq.count("A"), seq.count("C"), seq.count("G"), seq.count("T")


def main():
    seqs = get_seq(DATA_FILE)
    count_A, count_C, count_G, count_T = count_dna_nucleotides(seqs[0])
    print(count_A, count_C, count_G, count_T)


if __name__ == "__main__":
    main()
