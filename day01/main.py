#!/usr/bin/env python3

with open("input.txt", 'r') as f:
    elf_fuel = list(map(
                   lambda elf_cal_chunks : sum(map(
                                       lambda calorie_amt : int(calorie_amt),  # convert each number to int
                                       elf_cal_chunks.split("\n")              # get each line in an elf chunk
                                    )),
                   f.read().split("\n\n")))                                    # split the data into each elf's chunks

print(max(elf_fuel))
print(sum(sorted(elf_fuel)[-3:]))