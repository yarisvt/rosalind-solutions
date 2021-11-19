from math import comb
import os
import itertools

from util import MONOISOTOPIC_MASS_TABLE

DATA_FILE = os.path.join("../data", "rosalind_spec.txt")


def get_data(file: str) -> list[float]:
    with open(file, "r") as f:
        return list(map(float, f.readlines()))


def get_possible_proteins(masses: list[float]) -> str:
    prot = [""]
    for i in range(len(masses) - 1):
        mass = masses[i + 1] - masses[i]
        new_prot = [
            aa
            for aa, aa_mass in MONOISOTOPIC_MASS_TABLE.items()
            if round(mass, 2) == round(aa_mass, 2)
        ]
        prot = [p + new_p for p in prot for new_p in new_prot]

    return prot[0]


def main():
    masses = get_data(DATA_FILE)
    weights = get_possible_proteins(masses)
    print(weights)


if __name__ == "__main__":
    main()
