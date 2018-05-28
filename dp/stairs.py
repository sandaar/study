def count_ways_to_climb(steps, n):
    # steps is a list of integers
    number_of_ways = [0] * (n + 1)
    number_of_ways[0] = 1
    for i in range(0, n + 1):
        if number_of_ways[i] != 0 or i == 0:
            for j in range(len(steps)):
                next_step = i + steps[j]
                if next_step <= n:
                    number_of_ways[next_step] += number_of_ways[i]
        print(i, number_of_ways)
    return number_of_ways[n]


if __name__ == '__main__':
    steps = [1, 2]
    n = 10
    result = count_ways_to_climb(steps, n)
    print(result)
