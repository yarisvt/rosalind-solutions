import os
from util import read_fasta_file

DATA_FILE = os.path.join("../data", "rosalind_lcsq.txt")


def get_common_longest_subsequence(s1, s2):
    matrix = [["" for _ in range(len(s2))] for _ in range(len(s1))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i == 0 or j == 0:
                    matrix[i][j] = s1[i]
                else:
                    matrix[i][j] = matrix[i-1][j-1] + s1[i]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], key=len)
    cs = matrix[-1][-1]
    return cs


def main():
    fasta_data = read_fasta_file(DATA_FILE)
    seqs = [seq for _, seq in fasta_data]
    common_longest_subsequence = get_common_longest_subsequence(seqs[0], seqs[1])
    print(common_longest_subsequence)


if __name__ == "__main__":
    main()
