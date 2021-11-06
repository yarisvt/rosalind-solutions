import os
import math

DATA_FILE = os.path.join("../data", "rosalind_pper.txt")


def get_data(file: str) -> list[int]:
    with open(file, "r") as f:
        return list(map(int, f.read().strip().split()))


def get_total_number_partial_permutations(n: int, k: int) -> int:
    return int((math.factorial(n) / (math.factorial(n - k))) % 1000000)


def main():
    n, k = get_data(DATA_FILE)
    nr_permutations = get_total_number_partial_permutations(n, k)
    print(nr_permutations)


if __name__ == "__main__":
    main()
