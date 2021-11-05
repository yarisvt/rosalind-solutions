import os
from util import read_fasta_file

DATA_FILE = os.path.join("../data", "rosalind_tran.txt")


TRANSITION = [("A", "G"), ("T", "C"), ("C", "T"), ("G", "A")]
TRANSVERSION = [
    ("A", "T"),
    ("A", "C"),
    ("T", "A"),
    ("T", "G"),
    ("C", "A"),
    ("C", "G"),
    ("G", "T"),
    ("G", "C"),
]


def get_transition_transversion_ratio(seq1: str, seq2: str) -> float:
    assert len(seq1) == len(seq2)

    transitions = 0
    transversions = 0
    for s1, s2 in zip(seq1, seq2):
        if (s1, s2) in TRANSITION:
            transitions += 1
        elif (s1, s2) in TRANSVERSION:
            transversions += 1

    if transversions == 0:
        return 0

    return transitions / transversions


def main():
    fasta_data = read_fasta_file(DATA_FILE)
    seqs = [seq for _, seq in fasta_data]
    ratio = get_transition_transversion_ratio(seqs[0], seqs[1])
    print(ratio)


if __name__ == "__main__":
    main()
