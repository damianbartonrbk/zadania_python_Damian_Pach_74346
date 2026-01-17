def hanoi(n, start, pomocniczy, cel):
    if n == 1:
        print(start, "->", cel)
    else:
        hanoi(n - 1, start, cel, pomocniczy)
        print(start, "->", cel)
        hanoi(n - 1, pomocniczy, start, cel)
hanoi(3, "A", "B", "C")