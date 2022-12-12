import util

lines = util.load_str_lines("input.txt")
x = 1
clock = 1
crt = set()


def draw(crt, clock, x):
    if (clock-1)%40 in range(x-1, x+2):
        crt.add(clock)


for i,line in enumerate(lines):
    match line.split():
        case ["addx", v]:
            clock += 1
            draw(crt, clock, x)
            clock += 1
            x += int(v)
        case ["noop"]:
            clock += 1
        case _:
            raise RuntimeError("Unexpected command " + line)

    draw(crt, clock, x)

print("Part2:") # FCJAPJRE
for i in range(6):
    row = []
    for j in range(40):
        if i*40+j in crt:
            row.append('#')
        else:
            row.append('.')
    print(''.join(row))