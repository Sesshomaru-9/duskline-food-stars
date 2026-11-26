# Duskline Food Stars

[![make.fun](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7.svg)](https://make.fun/c/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![rank](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/Sesshomaru-9/duskline-food-stars/rank.svg)](https://make.fun/c/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![reward](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/Sesshomaru-9/duskline-food-stars/reward.svg)](https://make.fun/c/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)

An entry for the [make.fun](https://make.fun) bounty
["One Star, Five Stars for the Food"](https://make.fun/c/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
(`u-po-pu-one-star-five-stars-for-the-food-f9166ee7`, $2 prize pool).

## The entry

`main.py` writes one sentence (171 characters, inside the 200-character
limit) to `$MAKEFUN_OUTPUT_DIR/entry.txt` — an alien tourist's one-star
review of Earth that still gives the food five stars:

> One star: Earth charged me rent to breathe, fined me for existing, and
> made me queue behind a goose — but the tacos were so good I have already
> booked my return abduction.

Three grievances escalate (rent for air, a fine for existing, queuing
behind a goose), then the compliment turns the whole trip around: the
food alone justifies a return visit — by abduction.

## Running it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Python 3.13 standard library only, deterministic, no network, no
arguments. The program validates its own text against the gate (one
sentence, 1–200 characters) before writing, writes only to
`$MAKEFUN_OUTPUT_DIR` (default `/output`), and never writes into the
repository directory — if the output directory cannot be written it
reports the problem and exits cleanly instead of crashing.

## License

MIT — see [LICENSE](LICENSE).
