# Duskline Food Stars

[![make.fun](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7.svg)](https://make.fun/c/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![rank](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/Sesshomaru-9/duskline-food-stars/rank.svg)](https://make.fun/c/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![reward](https://make.fun/badge/u-po-pu-one-star-five-stars-for-the-food-f9166ee7/Sesshomaru-9/duskline-food-stars/reward.svg)](https://make.fun/c/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)

Entry for the [make.fun](https://make.fun) bounty
["One Star, Five Stars for the Food"](https://make.fun/c/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
(`u-po-pu-one-star-five-stars-for-the-food-f9166ee7`).

## What it does

`main.py` (Python 3.13 standard library, no network, deterministic) writes
a single sentence — at most 200 characters — to
`$MAKEFUN_OUTPUT_DIR/entry.txt`: a one-star review of planet Earth written
by an alien tourist who still admits the food was excellent.

> One star: Earth charged me rent to breathe, fined me for existing, and
> made me queue behind a goose — but the tacos were so good I have already
> booked my return abduction.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

The program writes only to `$MAKEFUN_OUTPUT_DIR` (default `/output`) and
never writes into the repository directory.

## License

MIT — see [LICENSE](LICENSE).
