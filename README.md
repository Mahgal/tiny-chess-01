# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Mahgal/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Mahgal/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

Built for the make.fun bounty.

A tiny chess engine in a single 4 KB Python file — **4,096 bytes**, standard library only.

Play it via the make.fun competition: https://make.fun/bounty/tiny-chess-01

Referral: https://make.fun/r/6d6dq8sh

## Engine

- 0x88 board, pseudo-legal move generation with king-safety filtering
- Negamax with alpha-beta pruning, MVV-LVA move ordering, capture-only quiescence search
- Iterative deepening with a fixed node budget (~150,000 nodes per move, about 2–3 seconds)
- Material evaluation with incremental updates (no piece-square tables — the 4 KB budget went to search)
- Fully deterministic: fixed node budget, no clock, no randomness
- Talks UCI to the make.fun environment over HTTP (`/game`, `/move`)

## Files

- `main.py` — the whole engine (4,096 bytes)
- `README.md` — this file
- `LICENSE` — MIT

## Run

Set `MAKEFUN_ENV_URL` to the environment server URL and run:

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:18080 python3 main.py
```

## License

MIT — see `LICENSE`.
