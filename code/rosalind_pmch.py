import os
import math

from util import is_rna, read_fasta_file

DATA_FILE = os.path.join("../data", "rosalind_pmch.txt")


def get_data(file: str) -> list[int]:
    with open(file, "r") as f:
        return list(map(int, f.read().strip().split()))


def get_perfect_matches(seq: str) -> int:
    if not is_rna(seq):
        raise ValueError("sequence is not an RNA string")

    pmch = math.factorial(seq.count("A")) * math.factorial(seq.count("C"))
    return pmch


def main():
    fasta_data = read_fasta_file(DATA_FILE)
    seqs = [seq for _, seq in fasta_data]
    expected_nr_offspring = get_perfect_matches(seqs[0])
    print(expected_nr_offspring)


if __name__ == "__main__":
    main()
