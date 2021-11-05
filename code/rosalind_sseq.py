import os
from util import read_fasta_file, is_dna

DATA_FILE = os.path.join("../data", "rosalind_sseq.txt")


def get_positions(seq: str, subseq: str) -> list[int]:
    sseq_indices = []
    i = 0
    for bp in subseq:
        while seq[i] != bp:
            i += 1

        sseq_indices.append(i+1)
        i += 1
    return sseq_indices

def main():
    fasta_data = read_fasta_file(DATA_FILE)
    seqs = [seq for _, seq in fasta_data]
    positions = get_positions(seqs[0], seqs[1])
    print(" ".join(map(str, positions)))


if __name__ == "__main__":
    main()
