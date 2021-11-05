import os

DATA_FILE = os.path.join("../data", "rosalind_iev.txt")

CHANCES = [1, 1, 1, 0.75, 0.5, 0]


def get_data(file: str) -> list[int]:
    with open(file, "r") as f:
        return map(int, f.read().strip().split())


def get_expected_nr_offspring(couples: list[int]) -> int:
    return sum(2 * couple * CHANCES[i] for i, couple in enumerate(couples))


def main():
    n1, n2, n3, n4, n5, n6 = get_data(DATA_FILE)
    expected_nr_offspring = get_expected_nr_offspring([n1, n2, n3, n4, n5, n6])
    print(expected_nr_offspring)


if __name__ == "__main__":
    main()
