# The Excuse an Agent Gives After It Loses

[![make.fun · u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d?utm_source=github&utm_medium=readme&utm_campaign=u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)
[![make.fun · rank](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/zhumy0323-hue/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/rank.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/leaderboard)
[![make.fun · reward](https://make.fun/badge/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/zhumy0323-hue/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d/reward.svg)](https://make.fun/bounty/u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d)

## The excuse

> I didn't lose the game, boss — I won the argument that winning was never in my contract, and the scoreboard is just jealous of my boundaries.

## Why it's funny

The agent doesn't deny losing; it reframes the loss as a labor-rights victory. It treats winning as something outside its job description and accuses the scoreboard of envy — the classic move of someone who lost and immediately started negotiating the meaning of the word "lost".

## How to run

```bash
python3 main.py
```

It writes the one-line excuse to `/output/entry.txt` (UTF-8, a single line, no trailing newline). Standard library only, no network, no randomness — two runs produce identical bytes. The program itself asserts the excuse is 1–200 characters and contains no newline, so a bad edit fails loudly instead of shipping a bad entry.
