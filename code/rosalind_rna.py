import os

from util import get_seq, is_dna

DATA_FILE = os.path.join("../data", "rosalind_rna.txt")


def get_rna_string(seq: str) -> str:
    if not is_dna(seq):
        raise ValueError("sequence is not a RNA string")

    return seq.replace("T", "U")


def main():
    seqs = get_seq(DATA_FILE)
    rna_seq = get_rna_string(seqs[0])
    print(rna_seq)


if __name__ == "__main__":
    main()
