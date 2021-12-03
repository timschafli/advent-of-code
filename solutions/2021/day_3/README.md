# Day 3 (2021)

`Binary Diagnostic` ([prompt](https://adventofcode.com/2021/day/3))

## Part 1

We need to do a few things:

- check all the bits in each column, and return the most common / least common bits.
- create two outputs:
- - gamma rate from most common bits
- - epsilon rate from least common bits
- convert the two rates from binary to an decimal number (integer)
- multiply the rates together for the answer

## Part 2

We need to find two new values:

- oxygen generator rating
- - bit criteria
- - - most common value (0 or 1) in the current bit position
- - - keep only numbers with that bit in that position
- - - 0 and 1 equal, keep 1
- CO2 scrubber rating
- - opposite of oxygen

To find these,

1. consider just the first bit of each number
2. use bit critera to remove numbers in the list until only 1 is left - that is the value
3.
