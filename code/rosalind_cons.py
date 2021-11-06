import os
from util import read_fasta_file

DATA_FILE = os.path.join("../data", "rosalind_cons.txt")


def get_profile_matrix(seqs: list[str]) -> dict[str, list[int]]:
    len_seqs = len(seqs[0])
    profile_matrix = {
        "A": [0] * len_seqs,
        "C": [0] * len_seqs,
        "G": [0] * len_seqs,
        "T": [0] * len_seqs,
    }

    for seq in seqs:
        for i, nt in enumerate(seq):
            profile_matrix[nt][i] += 1

    return profile_matrix


def get_consesus_string(profile_matrix: dict[str, list[int]], length: int) -> str:
    max_occurrences = [0] * length
    consesus_string = [""] * length
    for nt, occurrences in profile_matrix.items():
        for i, occurrence in enumerate(occurrences):
            if occurrence > max_occurrences[i]:
                max_occurrences[i] = occurrence
                consesus_string[i] = nt
    return "".join(consesus_string)


def write_to_file(profile_matrix: dict[str, list[int]], consesus_string: str) -> None:
    with open(os.path.join("../data", "rosalind_cons_solutions.txt"), "w") as f:
        f.write(f"{consesus_string}\n")
        for nt, occ in profile_matrix.items():
            f.write(f"{nt}: {' '.join(map(str, occ))}\n")


def main():
    fasta_data = read_fasta_file(DATA_FILE)
    seqs = [seq for _, seq in fasta_data]
    profile_matrix = get_profile_matrix(seqs)
    consesus_string = get_consesus_string(profile_matrix, len(seqs[0]))

    # the matrix can become very large, so write to file
    write_to_file(profile_matrix, consesus_string)

    # print(consesus_string)
    # for nt, occ in profile_matrix.items():
    #     print(f"{nt}: {' '.join(map(str, occ))}")


if __name__ == "__main__":
    main()
