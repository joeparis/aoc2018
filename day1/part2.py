#! python3
# coding=utf-8
from time import time
from itertools import accumulate, cycle


# def io_heavy():
#     with open("input.txt", "r") as file:
#         accumulator = 0
#         frequencies = [0]
#         while True:
#             try:
#                 accumulator += int(file.readline().strip())
#                 if accumulator in frequencies:
#                     print(accumulator)
#                     break
#                 frequencies.append(accumulator)
#             except:
#                 file.seek(0)


# def in_mem():
#     with open("input.txt", "r") as file:
#         values = [int(value.strip()) for value in file.read().split()]
#     accumulator = 0
#     frequencies = [0]
#     idx = 0
#     while True:
#         accumulator += values[idx % len(values)]
#         if accumulator in frequencies:
#             print(accumulator)
#             break
#         frequencies.append(accumulator)
#         idx = (idx + 1) % len(values)


def main():
    seen = set()
    with open("input.txt", "r") as file:
        deltas = [int(value) for value in file.read().strip().split()]

    print(next(f for f in accumulate(cycle(deltas)) if f in seen or seen.add(f)))


if __name__ == "__main__":
    # # avg 95 seconds
    # start = time()
    # io_heavy()
    # end = time()
    # print(end - start)

    # # avg 95 seconds
    # start = time()
    # in_mem()
    # end = time()
    # print(end - start)

    # first two attempts are horrible, using the functionality provided
    # by the standard library is SO much better
    start = time()
    main()
    end = time()
    print(end - start)
