import sys
import itertools

ip = "mask = 000000000000000000000000000000X1001X\nmem[42] = 100\nmask = 00000000000000000000000000000000X0XX\nmem[26] = 1".split(
    '\n')
# ip = sys.stdin.read().split('\n')[:-1]
print(ip[-1])

instructions = []
current_mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
for s in ip:
    print(s)
    if s[1] == 'a':
        current_stack = []
        current_mask = s.split()[-1]
        instructions.append((current_mask, current_stack))
        print(current_mask)
    else:
        current_stack.append((f"{int(s.split(']')[0][4:]):036b}", f"{int(s.split('=')[-1]):036b}"))
print()
print(instructions)
print()

mem = dict()
for m, ops in instructions:
    for pos, v in ops:
        xs = []
        addr = [c for c in m]
        for i, p in enumerate(pos):
            if m[i] == '0':
                addr[i] = p
            elif m[i] == 'X':
                xs.append(i)
        print(''.join(addr))
        addrs = []
        for p in itertools.product('01', repeat=len(xs)):
            for i, xi in enumerate(xs):
                addr[xi] = p[i]
            addrs.append(int(''.join(addr), 2))

        for a in addrs:
            mem[a] = int(v, 2)
        print(pos, int(pos, 2), addrs)
        print()

print(sum(mem.values()))
