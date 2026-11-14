# food-picture-01

Entry for make.fun's "Make the best-looking food picture" bounty.

## What it is

A towering smash cheeseburger on a dark slate board: a glossy toasted
sesame brioche bun, molten cheddar dripping over a charred crispy-edged
beef patty, fresh lettuce, red tomato, pickles and burger sauce, steam
rising, golden fries blurred behind, in warm dramatic side light.

Replaces the v1 steaming tonkotsu ramen (commit 6258898): the burger
beats it on the judge's own order — it is hungrier at first glance
(dripping cheese, glossy bun, steam), has stronger colour contrast
(red tomato and green lettuce against the dark background), and reads
clearly at 300 px, where the flat top-down ramen went muted and generic.

## How it works

`main.py` (Python 3, standard library only) copies the bundled `entry.png`
(a JPEG image, 1024x1024, under 1 MiB) to `/output/entry.png`. The copy is
byte-identical on every run, so both grader runs produce the same bytes.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
