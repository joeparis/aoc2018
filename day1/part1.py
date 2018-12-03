#! python3
# coding=utf-8
from time import time


def main():
    with open("input.txt", "r") as file:
        deltas = [int(value) for value in file.read().strip().split()]
    print(sum(deltas))


if __name__ == "__main__":
    start = time()
    main()
    end = time()
    print(end - start)
