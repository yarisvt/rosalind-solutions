import os
import regex as re

from util import get_seq, is_dna

DATA_FILE = os.path.join("../data", "rosalind_subs.txt")


def find_motif_positions(seq: str, motif: str) -> list[int]:
    if not is_dna(seq):
        raise ValueError("sequence is not a DNA string")

    if not is_dna(motif):
        raise ValueError("motif is not a DNA string")

    # motif sequence should not be longer than the DNA sequence
    assert len(seq) > len(motif)

    motif_positions = []
    for match in re.finditer(rf"{motif}", seq, overlapped=True):
        motif_positions.append(match.span()[0] + 1)
    return motif_positions


def main():
    seqs = get_seq(DATA_FILE)
    positions = find_motif_positions(seqs[0], seqs[1])
    print(" ".join(map(str, positions)))


if __name__ == "__main__":
    main()
