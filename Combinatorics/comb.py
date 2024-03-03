import math
import sys


def choose(n: int, k: int) -> int:
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def subset(array: list, choices_binary: int) -> list:
    out = []

    for shift in range(len(array)):
        if ((choices_binary >> shift) & 1) == 1:
            out.append(array[shift])

    return out


def power_set(array: list) -> list:
    out = []
    for choices in range(2 ** len(array)):
        out.append(subset(array, choices))
    return out


def choose_subsets(array: list, k: int):
    p_set = power_set(array)
    p_set.sort()

    is_length_k = lambda arr: len(arr) == k
    [print(e) for e in filter(is_length_k, p_set)]


def comb(_, n, k, __, ___):
    nums = list(range(n))
    choose_subsets(nums, k)


if __name__ == "__main__":
    show_details = len(sys.argv) > 3  # Boolean on whether to print the inputs.
    total_count = int(sys.argv[1])
    starting_count = int(sys.argv[2])
    Array = []
    for i in range(starting_count):  # Creates an array of zeros with length k.
        Array.append(0)
    if show_details:
        print("n:", total_count, "k:", starting_count)
    comb(Array, total_count, starting_count, 0, 0)
