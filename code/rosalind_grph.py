import os
from util import read_fasta_file

DATA_FILE = os.path.join("../data", "rosalind_grph.txt")


def get_adjacency_list(fasta_info: list[list[str]], k=3) -> list[list[str]]:
    headers = [header for header, _ in fasta_info]
    seqs = [seq for _, seq in fasta_info]

    adjacency_list = []
    for i, seq1 in enumerate(seqs):
        for j, seq2 in enumerate(seqs):
            if i != j:
                if seq1[-k:] == seq2[:k]:
                    adjacency_list.append([headers[i], headers[j]])

    return adjacency_list


def main():
    fasta_data = read_fasta_file(DATA_FILE)
    adjacency_list = get_adjacency_list(fasta_data, k=3)
    for h1, h2 in adjacency_list:
        print(h1, h2)


if __name__ == "__main__":
    main()
