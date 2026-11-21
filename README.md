# tiny-chess-4k

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/kreutzx/tiny-chess-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/kreutzx/tiny-chess-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A complete chess engine in 4 KB of Python (standard library only), now in its v8 form: negamax alpha-beta search with null-move pruning, late move reductions, check extensions and quiescence search, ordered by MVV-LVA, killers and a history heuristic. The transposition table and history table persist across moves instead of being reset each turn, and the evaluation is incremental — material, piece-square scores, game phase, bishop counts, non-pawn material and the pawn lists are all maintained in make/unmake, which buys roughly 25–30% more nodes per second. On top of the tapered evaluation (piece-square tables, passed pawns) v8 tapers the bishop-pair bonus by game phase — worth +50 with all pieces on the board, rising to +100 in the endgame — and keeps the doubled- and isolated-pawn penalties read from those pawn lists. It searches a node budget set by game phase — 150,000 nodes per move in the opening and the endgame, 100,000 in the middlegame — no clock — so every game is deterministic. In the kit's practice gauntlet the shipped build scored 1,451 / 1,809 / 1,545 Elo across the three practice trials (mean ≈ 1,602), up from v6's ≈ 1,422, and it beat v6 head-to-head with a 60.0% score over 60 games.

## Run it

```sh
MAKEFUN_ENV_URL=<trial env url> MAKEFUN_TRIAL_SEED=1 python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=24q484pk&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
