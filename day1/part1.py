#! python3
# coding=utf-8


def main():
    deltas = []
    with open("input.txt", "r") as file:
        deltas = [int(value) for value in file.read().strip().split()]
    print(sum(deltas))


if __name__ == "__main__":
    main()
