import os
from util import read_fasta_file, is_dna, RNA_TO_ONE_PROTEIN

DATA_FILE = os.path.join("../data", "rosalind_splc.txt")


def remove_introns(seq: str, introns: list[str]) -> str:
    for intron in introns:
        if not is_dna(seq):
            raise ValueError("sequence is not a DNA string")
        seq = seq.replace(intron, "")
    return seq


def get_rna_string(seq: str) -> str:
    if not is_dna(seq):
        raise ValueError("sequence is not a DNA string")

    # length of string should be a multiple of 3 to translate RNA to protein
    assert (len(seq) % 3) == 0

    protein = ""
    for i in range(0, len(seq), 3):
        codon = seq[i : i + 3].replace("T", "U")
        amino_acid = RNA_TO_ONE_PROTEIN[codon]
        if amino_acid != "*":
            protein += amino_acid
    return protein


def main():
    fasta_data = read_fasta_file(DATA_FILE)
    seqs = [seq for _, seq in fasta_data]
    seq_removed_introns = remove_introns(seqs[0], seqs[1:])
    protein = get_rna_string(seq_removed_introns)
    print(protein)


if __name__ == "__main__":
    main()
