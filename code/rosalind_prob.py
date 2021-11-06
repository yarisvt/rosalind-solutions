import os
import math

DATA_FILE = os.path.join("../data", "rosalind_prob.txt")


def get_data(file: str) -> tuple[str, list[float]]:
    with open(file, "r") as f:
        return f.readline().strip(), list(map(float, f.readline().strip().split()))


def get_counts(seq: str) -> list[int]:
    return [seq.count("A") + seq.count("T"), seq.count("G") + seq.count("C")]


def get_probabilities(gc_contents: list[float], codon_count: list[int]) -> list[float]:
    probabilities: list[float] = []

    for gc in gc_contents:
        prob = (codon_count[0] * math.log10((1 - gc) / 2)) + (
            codon_count[1] * math.log10(gc / 2)
        )

        probabilities.append(prob)

    return probabilities


def main():
    seq, gc_contents = get_data(DATA_FILE)
    counts = get_counts(seq)
    probabilities = get_probabilities(gc_contents, counts)
    print(" ".join(map(str, probabilities)))


if __name__ == "__main__":
    main()
