filename = "C:\\Users\\Mohammed\\OneDrive\\VisualStudioCode\\AdventCode\\Day20\\adventday20input.txt"
import Machine as m

def part1(input: [str]):
    return m.Machine(input).start_broadcast(1000)

# see comments on start_RX in Machine.py to understand what happened.
def part2(input: [str]):
    return m.Machine(input).start_RX()

def main():
    input = open(filename, "r").read().splitlines()
    part1_sum = part1(input)
    print(f"Part 1: {part1_sum}")
    part2_sum = part2(input)
    print(f"Part 2: {part2_sum}")

if __name__ == "__main__":
    main()