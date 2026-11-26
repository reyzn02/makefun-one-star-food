# One Star, Five Stars for the Food

[![make.fun bounty](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![make.fun rank](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/reyzn02/makefun-one-star-food/rank.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![make.fun reward](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/reyzn02/makefun-one-star-food/reward.svg)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)

An entry for the [make.fun](https://make.fun) bounty **One Star, Five Stars for the Food**: one sentence, at most 200 characters, in the voice of an alien tourist giving planet Earth a one-star review while still slipping in a real compliment about the food.

## The entry

> One star: the locals dig a hole, bury perfectly good cabbage until it stinks, and serve the rot for dinner — but the kimchi was so good I asked for the recipe and the burial coordinates.

(186 characters, one sentence.)

The angle: an alien misreads kimchi fermentation as burying perfectly good cabbage until it stinks — outsider bafflement at a human habit, a grievance worth one star, and a compliment that lands as a punchline (asking for the recipe *and* the burial coordinates).

## How it works

`main.py` (Python 3, standard library only) validates the gate — UTF-8 text of 1 to 200 characters, not only whitespace, exactly one sentence — then writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
