import os
from util import read_fasta_file, DNA_COMPLEMENT

DATA_FILE = os.path.join("../data", "rosalind_corr.txt")


def get_reverse_complement(seq: str) -> str:
    return "".join([DNA_COMPLEMENT[bp] for bp in seq[::-1]])


def get_hamming_distance(seq1: str, seq2: str) -> int:
    hamm_distance = 0
    for s1, s2 in zip(seq1, seq2):
        if s1 != s2:
            hamm_distance += 1
    return hamm_distance


def get_all_seqs(seqs: list[str]) -> list[str]:
    all_seqs: list[str] = []
    for seq in seqs:
        all_seqs.append(seq)
        all_seqs.append(get_reverse_complement(seq))
    return all_seqs


def get_correct_and_incorrect_seqs(
    seqs: list[str], all_seqs: list[str]
) -> tuple[list[str], list[str]]:

    incorrect_seqs: list[str] = []
    correct_seqs: list[str] = []

    for seq in seqs:
        if all_seqs.count(seq) == 1:
            incorrect_seqs.append(seq)
        else:
            correct_seqs.append(seq)
    return correct_seqs, incorrect_seqs


def get_corrected_seqs(
    correct_seqs: list[str], incorrect_seqs: list[str]
) -> list[tuple[str, str]]:
    corrected_seqs: list[tuple[str, str]] = []

    for incorrect_seq in incorrect_seqs:
        for correct_seq in correct_seqs:
            if (get_hamming_distance(incorrect_seq, correct_seq) == 1) or (
                get_hamming_distance(incorrect_seq, get_reverse_complement(correct_seq))
            ) == 1:
                corrected_seqs.append((incorrect_seq, correct_seq))
                break
    return corrected_seqs


def write_to_file(seqs: list[tuple[str, str]]) -> None:
    with open(os.path.join("../data", "rosalind_corr_solution_mand.txt"), "w") as f:
        for seq in seqs:
            f.write(f"{'->'.join(seq)}\n")


def main():
    fasta_data = read_fasta_file(DATA_FILE)
    seqs = [seq for _, seq in fasta_data]
    all_seqs = get_all_seqs(seqs)
    correct_seqs, incorrect_seqs = get_correct_and_incorrect_seqs(seqs, all_seqs)
    corrected_seqs = get_corrected_seqs(correct_seqs, incorrect_seqs)

    # there can be many corrected seqs, so write to file
    write_to_file(corrected_seqs)

    # print("\n".join(map(lambda x: "->".join(x), corrected_seqs)))


if __name__ == "__main__":
    main()
