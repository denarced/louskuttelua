#!venv/bin/python
"""Remove duplicates."""

import json

from format import format_main_json

FILENAME = "epithets.json"
ROOT_PROPERTY = "epithets"


def read_epithets():
    with open(FILENAME, encoding="utf-8") as file:
        return json.load(file)


def write_epithets(epithets):
    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(epithets, file)


def without_duplicates(epithets):
    content = {}
    cleaned = {ROOT_PROPERTY: content}
    for epithet, mentions in epithets[ROOT_PROPERTY].items():
        content[epithet] = without_duplicate_dicts(mentions)
    return cleaned


def without_duplicate_dicts(dicts):
    seen = set()
    deduplicated = []
    for each in dicts:
        a_tuple = dict_to_tuple(each)
        if a_tuple in seen:
            continue
        seen.add(a_tuple)
        deduplicated.append(each)
    return deduplicated


def dict_to_tuple(dictionary):
    return tuple(dictionary.items())


def main():
    epithets = read_epithets()
    without = without_duplicates(epithets)
    write_epithets(without)
    format_main_json()


if __name__ == "__main__":
    main()
