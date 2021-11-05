import os
from functools import cache

from typing import Union, Callable

DATA_FILE = os.path.join("../data", "rosalind_fib.txt")


def get_data(file: str) -> list[int]:
    with open(file, "r") as f:
        return map(int, f.read().strip().split())


@cache  # cache results so calculations with same input have to be done only once (much faster)
def get_number_of_rabbits(months: int, k_offsptring: int) -> Union[int, Callable]:
    if months <= 2:
        return 1
    return get_number_of_rabbits(months - 1, k_offsptring) + (
        k_offsptring * get_number_of_rabbits(months - 2, k_offsptring)
    )


def main():
    months, k_offspring = get_data(DATA_FILE)
    number_of_rabbits = get_number_of_rabbits(months, k_offspring)
    print(number_of_rabbits)


if __name__ == "__main__":
    main()
