import os
from util import read_fasta_file

DATA_FILE = os.path.join("../data", "rosalind_lcsm.txt")


def get_longest_substring(seqs: list[str]) -> str:
    longest_substring = ""
    for start_index in range(len(seqs[0])):
        for end_index in range(len(seqs[0]), start_index, -1):
            if end_index - start_index <= len(longest_substring):
                break
            elif check_substring(seqs[0][start_index:end_index], seqs):
                longest_substring = seqs[0][start_index:end_index]

    return longest_substring


def check_substring(find_string: str, string_list: list[str]) -> bool:
    for string in string_list:
        if (len(string) < len(find_string)) or (find_string not in string):
            return False
    return True


def main():
    fasta_data = read_fasta_file(DATA_FILE)
    seqs = [seq for _, seq in fasta_data]
    longest_substring = get_longest_substring(seqs)
    print(longest_substring)


if __name__ == "__main__":
    main()
