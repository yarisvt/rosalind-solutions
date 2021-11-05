import os
from typing import Callable, Union
from util import read_fasta_file

DATA_FILE = os.path.join("../data", "rosalind_long.txt")


def get_shortest_superstring(superstring: str, seqs: list[str]) -> Union[str, Callable]:
    if not seqs:
        return superstring

    length_seq = len(seqs[0])
    for i in range(int(length_seq / 2), length_seq)[::-1]:
        for seq in seqs:
            if superstring[:i] == seq[-i:]:
                superstring = seq + superstring[i:]
                seqs.remove(seq)
                break
            elif superstring[-i:] == seq[:i]:
                superstring = superstring + seq[i:]
                seqs.remove(seq)
                break
            else:
                continue

    return get_shortest_superstring(superstring, seqs)


def main():
    fasta_data = read_fasta_file(DATA_FILE)
    seqs = [seq for _, seq in fasta_data]
    s = get_shortest_superstring(seqs[0], seqs[1:])
    print(s)


if __name__ == "__main__":
    main()
