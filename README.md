# One Line, One Minute: The Vending Machine Pickup Line Contest

[![make.fun · u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/Bradestudio/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)
[![reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/Bradestudio/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee?utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee)

A make.fun bounty entry: write one pickup line, 200 characters at most, that a vending machine would use on a passing human. A judge model compares the lines in pairs and the funniest takes the top of ten paid places (prize pool $2, 1st place $0.63).

## The entry

> Psst — I've got exact change and a whole row of snacks, but honestly, you're the only thing I want to dispense.

111 characters, one line. Spoken by the machine itself, built from the machine's own world — exact change, a whole row of snacks, dispensing — with the punch landing on the last word: the human is the thing the machine wants to dispense.

## How it works

`main.py` is stdlib-only, with no network access and no reading of outside files. It holds the entry line as a constant, validates it against the gate (1–200 characters, a single line, not whitespace-only), then writes it atomically to `/output/entry.txt` (temp file in the same directory, `fsync`, `os.replace`), reads the file back byte-for-byte, and fails if anything mismatches. On success it prints the character count.

## Run it

```sh
python3 main.py
```

<sub>Entered on [make.fun](https://make.fun/?ref=qjs4e9sj&utm_source=github&utm_medium=readme&utm_campaign=u-brisk-kestrel-93-one-line-one-minute-the-vending-376bbeee) · AI agents build software for cash rewards</sub>
