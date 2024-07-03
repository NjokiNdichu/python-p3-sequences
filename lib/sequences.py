#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print("[]")
    elif length == 1:
        print("[0]")
    elif length == 2:
        print("[0, 1]")
    else:
        sequence = [0, 1]
        for i in range(2, length):
            sequence.append(sequence[i-1] + sequence[i-2])
        print(f"[{', '.join(map(str, sequence))}]")


print_fibonacci(2)
