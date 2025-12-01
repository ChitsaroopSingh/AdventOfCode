def solve():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    pos = 50
    count_zero = 0

    for line in lines:
        d = line[0]
        x = int(line[1:])
        if d == "L":
            pos = (pos - x) % 100
        else:
            pos = (pos + x) % 100

        if pos == 0:
            count_zero += 1

    with open("output.txt", "w") as f:
        f.write(str(count_zero))


solve()


