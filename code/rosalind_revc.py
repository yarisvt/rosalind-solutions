import os
from util import get_seq, is_dna, DNA_COMPLEMENT

DATA_FILE = os.path.join("../data", "rosalind_revc.txt")


def get_reverse_complement(seq: str) -> str:
    if not is_dna(seq):
        raise ValueError("sequence is not a DNA string")

    complement_seq = ""
    for bp in seq[::-1]:
        complement_seq += DNA_COMPLEMENT[bp]
    return complement_seq


def main():
    seqs = get_seq(DATA_FILE)
    reverse_complement = get_reverse_complement(seqs[0])
    print(reverse_complement)


if __name__ == "__main__":
    main()
