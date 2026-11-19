# tiny-chess-4k

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/kreutzx/tiny-chess-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/kreutzx/tiny-chess-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A complete chess engine in 4 KB of Python (standard library only): negamax alpha-beta search with a transposition table, quiescence search, MVV-LVA and history move ordering, and a tapered evaluation (piece-square tables, bishop pair, passed pawns). It searches a fixed budget of 100,000 nodes per move — no clock — so every game is deterministic. In the kit's practice gauntlet it scored 2 wins, 1 draw, 3 losses against the house ladder (depth-2 through nodes-500k).

## Run it

```sh
MAKEFUN_ENV_URL=<trial env url> MAKEFUN_TRIAL_SEED=1 python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=24q484pk&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
