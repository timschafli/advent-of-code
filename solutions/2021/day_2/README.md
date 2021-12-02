# Day 2 (2021)

`Dive!` ([prompt](https://adventofcode.com/2021/day/2))

## Part 1

First, we need to split the input lines further to get both a direction and an amount value.
We'll also need to translate the direction and distance into two axis and an amount.

- Distance always increases
- Depth can be positive or negative
- Created a `parseInstruction` method for parsing our array of string line inputs:

```py
def parseInstruction(inputLine):
    direction, distance = inputLine.split()
    distance = int(distance)
    return {
        "forward": {"distance": distance, "depth": 0},
        "down": {"distance": 0, "depth": distance},
        "up": {"distance": 0, "depth": distance * -1},
    }[direction]
```

After fully parsing the input, we can simply sum the `distance`s and `depth`s, multiply them together, and have our answer.

## Part 2

Little bit trickier here where we move by adjusting aim and then using that aim to move
We'll need to process each instruction, but we can still use the `parseInstruction` method we defined in Part 1 to get started.

This time we'll start our `aim`, `distance`, and `depth` all at 0, then use the following loop to run through the instruction data:

```py
for instruction in instructions:
    aim += instruction["depth"]
    distance += instruction["distance"]
    depth += aim * instruction["distance"]
```

Once again, mutliply `distance` & `depth` to get our answer.
