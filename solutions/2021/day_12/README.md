# Day 12 (2021)

`Passage Pathing` ([prompt](https://adventofcode.com/2021/day/12))

## Part 1

We need to get a list of cave connections pairs.
Create an list of lists for possible paths.
Start with one list of just "start"
Run a Loop until all lists end with "end"
For each loop, when evaluating which way to go, duplicate the list if there is more than 1 option
Anytime a list contains more than 1 copy of lowercase cave, delete that list.
Stop evaluating lists when they contain "end"

## Part 2
