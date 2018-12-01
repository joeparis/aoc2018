#! python3
# coding=utf-8
import time


def io_heavy():
    with open("test3.txt", "r") as file:
        accumulator = 0
        frequencies = [0]
        while True:
            try:
                accumulator += int(file.readline().strip())
                if accumulator in frequencies:
                    print(accumulator)
                    break
                frequencies.append(accumulator)
            except:
                file.seek(0)


def in_mem():
    values = []
    file = open("test3.txt", "r")
    while True:
        value = file.readline()
        if value == "":
            break
        value = value.strip()
        value = int(value)
        values.append(value)
    file.close()
    accumulator = 0
    frequencies = [0]
    idx = 0
    while True:
        accumulator += values[idx % len(values)]
        if accumulator in frequencies:
            print(accumulator)
            break
        frequencies.append(accumulator)
        idx += 1


if __name__ == "__main__":
    # avg 95 seconds
    start = time.time()
    io_heavy()
    end = time.time()
    print(end - start)

    # avg 95 seconds
    start = time.time()
    in_mem()
    end = time.time()
    print(end - start)
