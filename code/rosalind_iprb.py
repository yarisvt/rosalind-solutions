import os
from functools import cache

from typing import Union, Callable

DATA_FILE = os.path.join("../data", "rosalind_iprb.txt")


def get_data(file: str) -> list[int]:
    with open(file, "r") as f:
        return map(int, f.read().strip().split())


def get_probability(hom: int, het: int, rec: int) -> float:
    # The number of potential children who display the recessive gene.
    total = (het * het) + (4 * rec * rec) + (4 * het * rec) - (4 * rec) - het

    # The number of potential children who display the recessive gene.
    total_rec = 4 * (hom + het + rec) * (hom + het + rec - 1)

    # Using the complementary event to find the probability of a dominant gene expression.
    return 1 - float(total) / total_rec


def main():
    k_homozygous, m_heterozygous, n_recessive = get_data(DATA_FILE)
    number_of_rabbits = get_probability(k_homozygous, m_heterozygous, n_recessive)
    print(number_of_rabbits)


if __name__ == "__main__":
    main()
