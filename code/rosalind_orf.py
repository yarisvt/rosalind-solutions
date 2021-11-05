import os
from util import read_fasta_file, RNA_COMPLEMENT, RNA_TO_ONE_PROTEIN

DATA_FILE = os.path.join("../data", "rosalind_orf.txt")


def get_orf(seq: str) -> str:
    if len(seq) % 3 != 0:
        return seq[: -(len(seq) % 3)]
    return seq


def get_complement(seq: str) -> str:
    complement_seq = ""
    for bp in seq:
        complement_seq += RNA_COMPLEMENT[bp]
    return complement_seq


def get_different_orfs(seq: str) -> list[str]:
    seq = seq.replace("T", "U")  # from DNA to RNA

    return [
        get_orf(seq),
        get_orf(seq[1:]),
        get_orf(seq[2:]),
        get_complement(get_orf(seq[::-1])),
        get_complement(get_orf(seq[::-1][1:])),
        get_complement(get_orf(seq[::-1][2:])),
    ]


def get_protein(seq: str) -> str:
    protein = ""
    for i in range(0, len(seq), 3):
        aa = RNA_TO_ONE_PROTEIN[seq[i : i + 3]]
        protein += aa
        if aa == "*":
            break

    return protein.strip("*") if "*" in protein else ""


def get_proteins(seqs: list[str]) -> list[str]:
    proteins = []
    for seq in seqs:
        for i in range(0, len(seq), 3):
            aa = RNA_TO_ONE_PROTEIN[seq[i : i + 3]]
            if aa == "M":
                protein = get_protein(seq[i:])
                if protein:
                    proteins.append(protein)
    return proteins


def main():
    fasta_data = read_fasta_file(DATA_FILE)
    seqs = [seq for _, seq in fasta_data]
    orfs = get_different_orfs(seqs[0])
    proteins = get_proteins(orfs)
    print("\n".join(list(set(proteins))))


if __name__ == "__main__":
    main()
