# Day 6 (2021)

`Lanternfish` ([prompt](https://adventofcode.com/2021/day/6))

## Part 1

We're asked to model a growing population of fish over many days that have a pretty quick spawn rate.

The first thought that came to mind was to create a list of fish with their timers,
but looking at how quickly the fish multiply and how many days we're tracking them,
we know that that array would get expponentially large very quickly. If previous
AoC's are a guide, I would guess that Part 2 will be very similar but over many more days.

The second thought I had was that there would be many fish on the same step of the timer,
so with that in mind, we can instead track how many fish are at each step of the timer.
This means we only need a list of 9 integers and we can track the population for a long
time until the population goes out of range of integers.

First, we create an empty list. Then, we take the input, which represents multiple fishes, and groups them into the elements of the array.

For each day's advance, we pop the first element out of the array for spawning fish and add that number to the current 6 count fish and add a new element to the end of the array
representing the newly spawned fish.

Finally, input a number of days, repeat the process, then sum together each group of
counter classified fish for the answer.

## Part 2

Same, just larger number
