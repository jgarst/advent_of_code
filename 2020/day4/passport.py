"""
You arrive at the airport only to realize that you grabbed your North Pole
Credentials instead of your passport.
While these documents are extremely similar, North Pole Credentials aren't
issued by a country and therefore aren't actually valid documentation for travel
in most of the world.

It seems like you're not the only one having problems, though; a very long line
has formed for the automatic passport scanners, and the delay could upset your
travel itinerary.

Due to some questionable network security, you realize you might be able to
solve both of these problems at the same time.

The automatic passport scanners are slow because they're having trouble
detecting which passports have all required fields. The expected fields are as
follows:

- byr (Birth Year)
- iyr (Issue Year)
- eyr (Expiration Year)
- hgt (Height)
- hcl (Hair Color)
- ecl (Eye Color)
- pid (Passport ID)
- cid (Country ID)

Passport data is validated in batch files (your puzzle input).
Each passport is represented as a sequence of key:value pairs separated by
spaces or newlines.
Passports are separated by blank lines.

Here is an example batch file containing four passports:

> ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
> byr:1937 iyr:2017 cid:147 hgt:183cm

> iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
> hcl:#cfa07d byr:1929

> hcl:#ae17e1 iyr:2013
> eyr:2024
> ecl:brn pid:760753108 byr:1931
> hgt:179cm

> hcl:#cfa07d eyr:2025 pid:166559648
> iyr:2011 ecl:brn hgt:59in

The first passport is valid - all eight fields are present.
The second passport is invalid - it is missing hgt (the Height field).

The third passport is interesting; the only missing field is cid, so it looks
like data from North Pole Credentials, not a passport at all!
Surely, nobody would mind if you made the system temporarily ignore missing cid
fields.
Treat this "passport" as valid.

The fourth passport is missing two fields, cid and byr. Missing cid is fine,
but missing any other field is not, so this passport is invalid.

According to the above rules, your improved system would report 2 valid
passports.

Count the number of valid passports - those that have all required fields.
Treat cid as optional. In your batch file, how many passports are valid?
"""

import pathlib
import itertools
from collections.abc import Iterable
from typing import NamedTuple
import re

INPUT_PATH = pathlib.Path("input.txt")
PASSPORT_DELIMITER = re.compile("^\n$")
REQUIRED_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def passport_delimiter(line: str) -> bool:
    """Returns true is this line separates distinct passport inputs."""
    return PASSPORT_DELIMITER.match(line) is None


class Passport(NamedTuple):
    """The fields and metadata associated with a passport."""

    is_valid: bool


def count_valid_passports(passport_input: Iterable[str]) -> int:
    """
    Returns the number of distinct passports that contain the fields `byr`,
    `iyr`, `eyr`, `hgt`, `hcl`, `ecl`, and `pid`
    """
    passports = (
        parse_passport(text)
        for is_passport, text in itertools.groupby(
            passport_input, passport_delimiter
        )
        if is_passport
    )

    return sum(1 for passport in passports if passport.is_valid)


def parse_passport(lines: Iterable[str]) -> Passport:
    """
    Accepts an individual passport split among multiple lines, and returns a
    Passport tuple containing the structured data.
    """
    fields = {field[:3] for line in lines for field in line.split()}

    return Passport(is_valid=REQUIRED_FIELDS.issubset(fields))


def main() -> None:

    with open(INPUT_PATH) as passport_input:
        input_count = count_valid_passports(passport_input)

    print(f"The example file has {input_count} inputs")


if __name__ == "__main__":
    main()
