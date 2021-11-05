import os

from util import get_seq, is_rna, RNA_TO_ONE_PROTEIN

DATA_FILE = os.path.join("../data", "rosalind_prot.txt")


def get_protein(seq: str) -> str:
    if not is_rna(seq):
        raise ValueError("sequence is not a DNA string")

    # length of string should be a multiple of 3 to translate RNA to protein
    assert (len(seq) % 3) == 0

    protein = ""
    for i in range(0, len(seq), 3):
        protein += RNA_TO_ONE_PROTEIN[seq[i : i + 3]]
    return protein


def main():
    seqs = get_seq(DATA_FILE)
    protein = get_protein(seqs[0])
    print(protein)


if __name__ == "__main__":
    main()
