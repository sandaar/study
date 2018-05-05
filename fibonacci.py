def fibonacci():
    a, b = 1, 1
    yield a
    yield b
    a += b
    b += a
    yield a
    yield b

if __name__ == '__main__':
    fibonacci()
