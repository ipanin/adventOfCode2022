import util

lines = util.load_str_lines("input.txt")
x = 1
clock = 1
p1 = 0
times = range(20,221,40)
for i,line in enumerate(lines):
    match line.split():
        case ["addx", v]:
            clock += 1
            if clock in times:
                p1 += clock*x
            clock +=1
            x += int(v)
        case ["noop"]:
            clock += 1
        case _:
            raise RuntimeError("Unexpected command " + line)
    if clock in times:
        p1 += clock * x
    # print(f"{line:8} x={x}\tclock={clock}")

print("Part1", p1)  # 12880