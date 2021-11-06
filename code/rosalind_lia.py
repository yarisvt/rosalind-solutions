import os
import math

DATA_FILE = os.path.join("../data", "rosalind_lia.txt")


def get_data(file: str) -> list[int]:
    with open(file, "r") as f:
        return list(map(int, f.read().strip().split()))


def get_probability_at_least(n: int, k: int) -> float:
    prob_AaBb = 4 / 16.0
    total = 2 ** k
    prob = 0.0
    for i in range(n, 2 ** k + 1):
        prob += (
            math.comb(total, i) * (prob_AaBb ** i) * ((1 - prob_AaBb) ** (total - i))
        )
    return prob


def main():
    k, n = get_data(DATA_FILE)
    probability = get_probability_at_least(n, k)
    print(probability)


if __name__ == "__main__":
    main()
