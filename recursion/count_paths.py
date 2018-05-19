def count_paths(gw, gh, r, c):
    if r == gh or c == gw:
        return 0

    if r == gh - 1 or c == gw - 1:
        return 1

    return count_paths(gw, gh, r + 1, c) + count_paths(gw, gh, r, c + 1)


if __name__ == '__main__':
    print(count_paths(3, 2, 0, 0))
