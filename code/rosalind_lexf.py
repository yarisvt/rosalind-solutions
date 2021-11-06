import os
import itertools

from typing import Iterable

DATA_FILE = os.path.join("../data", "rosalind_lexf.txt")


def get_data(file: str) -> tuple[str, int]:
    with open(file, "r") as f:
        return f.readline().strip().replace(" ", ""), int(f.readline())


def get_products(alphabet: str, n: int) -> list[Iterable[str]]:
    return list(itertools.product("".join(alphabet), repeat=n))


def main():
    alphabet, n = get_data(DATA_FILE)
    produts = get_products(alphabet, n)
    print("\n".join(map(lambda x: "".join(map(str, x)), produts)))


if __name__ == "__main__":
    main()
