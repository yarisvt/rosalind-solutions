import os
from util import read_fasta_file, is_dna

DATA_FILE = os.path.join("../data", "rosalind_gc.txt")


def get_gc(seq: str) -> float:
    if not is_dna(seq):
        raise ValueError("sequence is not a DNA string")

    return (seq.count("G") + seq.count("C")) / len(seq)


def get_highest_gc(fasta_info: list[list[str, str]]) -> tuple[str, float]:
    highest_gc = 0
    header_highest_gc = None
    for header, seq in fasta_info:
        gc_percentage = get_gc(seq)
        if gc_percentage > highest_gc:
            highest_gc = gc_percentage
            header_highest_gc = header

    return header_highest_gc, highest_gc


def main():
    fasta_data = read_fasta_file(DATA_FILE)
    header_highest_gc, highest_gc = get_highest_gc(fasta_data)
    print(f"{header_highest_gc}\n{highest_gc*100}")


if __name__ == "__main__":
    main()
