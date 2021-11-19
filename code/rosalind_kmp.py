import re
import os

from util import read_fasta_file

DATA_FILE = os.path.join("../data", "rosalind_kmp.txt")


def get_failure_array(seq: str) -> list[int]:
    failure_array: list[int] = [0] * len(seq)
    longest_motif_length = 0

    for i in range(1, len(seq)):
        for j in range(1, len(seq) - i + 1):
            if seq[:i] == seq[j : j + i]:
                failure_array[j + i - 1] = len(seq[:i])
                longest_motif_length = len(seq[:i])

        if longest_motif_length < len(seq[:i]):
            break

    return failure_array


def write_to_file(failure_array: list[int]) -> None:
    with open(os.path.join("../data", "rosalind_kmp_solution.txt"), "w") as f:
        f.write(" ".join(map(lambda x: str(x), failure_array)))


def main():
    fasta_data = read_fasta_file(DATA_FILE)
    failure_array = get_failure_array(fasta_data[0][1])
    write_to_file(failure_array)

    # print(" ".join(map(lambda x: str(x), failure_array)))


if __name__ == "__main__":
    main()
