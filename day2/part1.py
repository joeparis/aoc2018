#! python3
# coding=utf-8
from collections import Counter


def main():
    with open("input.txt") as file:
        ids = file.read().strip().splitlines()
    counts = [0, 0]
    for id_ in ids:
        letter_frequencies = [letter for id_, letter in Counter(id_).most_common()]
        if 2 in letter_frequencies:
            counts[0] += 1
        if 3 in letter_frequencies:
            counts[1] += 1
    print(letter_frequencies)
    print(counts)

    return counts[0] * counts[1]


if __name__ == "__main__":
    print(main())
