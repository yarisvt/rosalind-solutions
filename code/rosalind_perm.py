import os
import itertools
from typing import Iterable

DATA_FILE = os.path.join("../data", "rosalind_perm.txt")


def get_data(file: str) -> int:
    with open(file, "r") as f:
        return int(f.read().strip())


def get_permutations(n: int) -> list[Iterable[int]]:
    list_n = list(range(1, n + 1))
    return list(itertools.permutations(list_n))


def write_to_file(permutations: list[Iterable[int]]) -> None:
    with open(os.path.join("../data", "rosalind_perm_solution.txt"), "w") as f:
        f.write(f"{len(permutations)}\n")
        for p in permutations:
            f.write(f"{' '.join(map(str, p))}\n")


def main():
    n = get_data(DATA_FILE)
    permutations = get_permutations(n)

    # there can be many permutatins, so write to file
    write_to_file(permutations=permutations)

    # print(len(permutations))
    # print("\n".join(map(lambda x: " ".join(map(str, x)), permutations)))


if __name__ == "__main__":
    main()
