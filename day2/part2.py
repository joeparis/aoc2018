#! python3
# coding=utf-8
from collections import Counter


def main():
    with open("test2.txt") as file:
        ids = file.read().strip().splitlines()
    for id1 in ids:
        for id2 in ids:
            delta = 0
            for idx, char in enumerate(id1):
                if char != id2[idx]:
                    delta += 1
            if delta == 1:
                answer = [char for idx, char in enumerate(id1) if id2[idx] == char]
                return "".join(answer)


if __name__ == "__main__":
    print(main())
