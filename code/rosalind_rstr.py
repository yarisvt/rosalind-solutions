import os

DATA_FILE = os.path.join("../data", "rosalind_rstr.txt")


def get_data(file: str) -> tuple[int, float, str]:
    with open(file, "r") as f:
        line_1 = list(map(float, f.readline().strip().split()))
        return int(line_1[0]), line_1[1], f.readline().strip()


def get_counts(seq: str) -> list[int]:
    return [seq.count("A") + seq.count("T"), seq.count("G") + seq.count("C")]


def get_probability(n: int, probability: float, codon_count: list[int]) -> float:
    dna_prob = (((1 - probability) / 2) ** codon_count[0]) * (
        (probability / 2) ** codon_count[1]
    )
    return 1 - ((1 - dna_prob) ** n)


def main():
    n, probability, seq = get_data(DATA_FILE)
    codon_count = get_counts(seq)
    probabilities = get_probability(n, probability, codon_count)
    print(probabilities)


if __name__ == "__main__":
    main()
