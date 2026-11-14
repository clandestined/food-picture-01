# food-picture-01

Entry for make.fun's "Make the best-looking food picture" bounty.

## What it is

A steaming bowl of tonkotsu ramen: golden glistening broth, springy noodles,
a jammy soft egg with a glossy orange yolk, chashu pork, nori, scallions and
sesame in a dark ceramic bowl, shot from above in warm light.

## How it works

`main.py` (Python 3, standard library only) copies the bundled `entry.png`
(a JPEG image, 1024x1024, under 1 MiB) to `/output/entry.png`. The copy is
byte-identical on every run, so both grader runs produce the same bytes.

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
