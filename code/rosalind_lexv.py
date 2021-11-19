import os
import itertools


DATA_FILE = os.path.join("../data", "rosalind_lexv.txt")


def get_data(file: str) -> tuple[str, int]:
    with open(file, "r") as f:
        return f.readline().strip(), int(f.readline())


def get_ordered_strings(aphabet: str, n: int) -> list[str]:
    split_alphabet = ["*"] + aphabet.split()

    ordered_strings: list[str] = []

    for item in itertools.product(split_alphabet, repeat=n):
        if "*" not in item:
            ordered_strings.append("".join(item))
        else:
            for i in range(1, n):
                if "".join(item[i:n]) == "*" * (n - i) and "*" not in item[:i]:
                    ordered_strings.append("".join(item).replace("*", ""))

    return ordered_strings


def write_to_file(ordered_strings: list[str]) -> None:
    with open(os.path.join("../data", "rosalind_lexv_solution.txt"), "w") as f:
        f.write("\n".join(ordered_strings))


def main():
    alphabet, n = get_data(DATA_FILE)
    ordered_strings = get_ordered_strings(alphabet, n)
    write_to_file(ordered_strings)

    # print("\n".join(produts))


if __name__ == "__main__":
    main()
