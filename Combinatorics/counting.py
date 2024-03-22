import sys

coins = [1, 5, 10, 25]


def partitions(n, max_partitions, current_partitions=0):
    if n <= 0:
        if current_partitions < max_partitions:
            return 0
        else:
            return 1

    if current_partitions == 0:
        return partitions(n - 1, max_partitions, 1)

    if current_partitions >= max_partitions:
        return current_partitions * partitions(n - 1, max_partitions, current_partitions)

    new_partition = partitions(n - 1, max_partitions, current_partitions + 1)
    add_partition = current_partitions * partitions(n - 1, max_partitions, current_partitions)

    return new_partition + add_partition


coins = [1, 5, 10, 25]
def make_change(total, current_coin=3):
    """
     given coin set {1,5,10,25} count how many ways we can pay amount a,
     c indicates which coin is considered first.  c starts as the index
     of the last coin value (len(coins)-1)
    """
    if current_coin == 0:
        return 1

    count = 0
    coin_value = coins[current_coin]
    replacement_value = 0
    while replacement_value <= total:
        count += make_change(total - replacement_value, current_coin-1)
        replacement_value += coin_value

    return count


if __name__ == "__main__":
    # partititions
    d = len(sys.argv) > 3
    n = int(sys.argv[1])
    k = int(sys.argv[2])
    p = partitions(n, k)
    print("n:", n, "k:", k, "partitions:", p)

    # make change
    c = len(coins) - 1
    a = 10 * n + k
    ways = make_change(a, c)
    print("amount:", a, "coins:", coins, "ways:", ways)
