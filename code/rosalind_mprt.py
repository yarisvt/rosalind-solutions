import os
import re

from io import StringIO
from Bio import SeqIO

from util import get_fasta_from_uniprot_id

DATA_FILE = os.path.join("../data", "rosalind_mprt.txt")
N_GLYCOSYLATION_PATTERN = r"(?=N[ARNDBCEQZGHILKMFSTWYV][ST][ARNDBCEQZGHILKMFSTWYV])"


def get_seq_from_fasta_string(fasta_string: str) -> str:
    fasta_io = StringIO(fasta_string)
    fasta_sequences = SeqIO.parse(fasta_io, format="fasta")
    seq = next(fasta_sequences)
    return str(seq.seq)


def get_data(file_protein_ids: str) -> dict[str, str]:
    data = {}
    with open(file_protein_ids, "r") as f:
        for protein_id in f:
            fasta = get_fasta_from_uniprot_id(protein_id.strip())
            seq = get_seq_from_fasta_string(fasta)
            data[protein_id.strip()] = seq
    return data


def find_protein_motif_positions(data: dict[str, str]) -> dict[str, str]:
    positions_data = {}
    for protein_id, seq in data.items():
        positions = get_positions(seq)
        positions_data[protein_id] = positions
    return positions_data


def get_positions(seq: str) -> str:
    match = re.finditer(N_GLYCOSYLATION_PATTERN, seq)
    positions = ""
    for j, pos in enumerate(match):
        if j > 0:
            positions += " "
        positions += str(pos.start() + 1)
    return positions


def main():
    data = get_data(DATA_FILE)
    positions_data = find_protein_motif_positions(data)
    for protein_id, positions in positions_data.items():
        if positions:
            print(f"{protein_id}\n{positions}")


if __name__ == "__main__":
    main()
