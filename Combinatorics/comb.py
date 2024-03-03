import sys





def digit_list(val, base):
    digits = []
    while val > 0:
        digits.append(val % base)
        val = val // base
    return digits


def unique_list(array):
    for i in range(len(array)-1):
        if array[i] in array[i+1:]:
            return False


def subsets(array, length):
    pass

def comb(_, n, __, p=0, lo=0):
    array = set(range(1, n+1))




if __name__ == "__main__":
    show_details = len(sys.argv) > 3  # Boolean on whether to print the inputs.
    total_count = int(sys.argv[1])  #
    starting_count = int(sys.argv[2])
    Array = []
    for i in range(starting_count):  # Creates an array of zeros with length k.
        Array.append(0)
    if show_details:
        print("n:", total_count, "k:", starting_count)
    comb(Array, total_count, starting_count)
