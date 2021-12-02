# Day 1 (2021)

`Sonar Sweep` ([prompt](https://adventofcode.com/2021/day/1))

## Part 1 (1559)

Seems straightforward so far. Used Python iterator to loop through the values, checking if the depth increased for each element in the array. Quick success.

## Part 2 (1600)

Hmm, tried to use slice and sum to get the groups to compare against each other. Came out with 1643 on first attempt, which was incorrect.
Turns out the solution of using slice and sum in a for loop did work, but I was missing the last group due to an off by 1 error.

Looked at another solution on reddit for Part 2:

    mov_sum = [d1 + d2 + d3 for d1, d2, d3 in zip(depths[2:], depths[1:-1], depths[:-2])]
    diffs = [dep - dep_os for dep, dep_os in zip(mov_sum[:-1], mov_sum[1:])]
    print(sum(1 for i in diffs if i < 0))

Learned about how Python list comprehensions, Zip objects creating tuples, and the combination of three differently sliced versions of depths works in conjunction to get a list of sums and then a list of diffs

Tried to think of a way to make this work dynamically where you could specify the size of the data window we're checking, but I couldn't find a way to make that dynamic.

Maybe something like `mov_sum = [sum(depths_in_window) for *dargs in zip(*daargs)] ???` I'll have to revisit this.
