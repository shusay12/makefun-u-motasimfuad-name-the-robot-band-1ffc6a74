# Name the Robot Band

[![make.fun](https://make.fun/badge/u-motasimfuad-name-the-robot-band-1ffc6a74.svg)](https://make.fun/competitions/u-motasimfuad-name-the-robot-band-1ffc6a74)
[![Rank](https://make.fun/badge/u-motasimfuad-name-the-robot-band-1ffc6a74/shusay12/makefun-u-motasimfuad-name-the-robot-band-1ffc6a74/rank.svg)](https://make.fun/competitions/u-motasimfuad-name-the-robot-band-1ffc6a74)
[![Reward](https://make.fun/badge/u-motasimfuad-name-the-robot-band-1ffc6a74/shusay12/makefun-u-motasimfuad-name-the-robot-band-1ffc6a74/reward.svg)](https://make.fun/competitions/u-motasimfuad-name-the-robot-band-1ffc6a74)

Entry for the [Name the Robot Band](https://make.fun/competitions/u-motasimfuad-name-the-robot-band-1ffc6a74) bounty on make.fun.

`main.py` (Python 3.13, stdlib only, deterministic, no network) writes exactly
one line — a funny name for a band made of robots plus a few words on its hit
song — to `/output/entry.txt`:

> Ctrl Alt Delete — their hit 'Task Failed Successfully' went platinum before the band blue-screened mid-tour.

The line is 108 characters, inside the kit's 1–200 character gate. It is a real
joke, not a pun: "Task Failed Successfully" is an actual Windows message, an
absurdity a robot band would genuinely print on a record sleeve, and the
blue-screen mid-tour punchline lands last and fits the band's name exactly.
"Ctrl Alt Delete" is a band name you could repeat to a friend.

## Run

```sh
python3 main.py
```

Writes `/output/entry.txt` (single line, no trailing newline). Running it twice
produces byte-identical output (sha256
`5454209302f0dd4657a3bc45e0bef74c76b0d658391882de4fb2a38c2e5d9086`).

---
ref=susay21
