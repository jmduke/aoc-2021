from typing import Counter, Dict

AGE = 7
BACKOFF = 2
DAYS = 256

def job(age_to_count: Dict[int, int], days: int) -> int:
    if days == 0:
        return sum(age_to_count.values())
    updated_age_to_count = {k - 1: v for k, v in age_to_count.items()}
    if -1 in updated_age_to_count:
        updated_age_to_count[AGE - 1] = updated_age_to_count.get(AGE - 1,0) + updated_age_to_count[-1]
        updated_age_to_count[AGE + BACKOFF - 1] = updated_age_to_count[-1]
        del updated_age_to_count[-1]
    return job(updated_age_to_count, days - 1)

def main(filename: str) -> int:
    with open(filename) as f:
        raw_ages = f.read().split(",")
        return job(Counter([int(age) for age in raw_ages]), DAYS)


print(main('6-1.txt'))
print(main('6-2.txt'))