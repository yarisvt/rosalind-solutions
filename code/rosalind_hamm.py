import os
from util import get_seq, is_dna

DATA_FILE = os.path.join("../data", "rosalind_hamm.txt")


def get_hamming_distance(seq1: str, seq2: str) -> int:
    if not is_dna(seq1):
        raise ValueError("sequence 1 is not a DNA string")
    
    if not is_dna(seq2):
        raise ValueError("sequence 2 is not a DNA string")

    # hamming distance assumes that the lenght of two strings are the same
    assert len(seq1) == len(seq2)

    hamm_distance = 0
    for s1, s2 in zip(seq1, seq2):
        if s1 != s2:
            hamm_distance += 1
    return hamm_distance

def main():
    seqs = get_seq(DATA_FILE)
    hamm_distance = get_hamming_distance(seqs[0], seqs[1])
    print(hamm_distance)


if __name__ == "__main__":
    main()
