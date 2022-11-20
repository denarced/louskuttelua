#!venv/bin/python

import json


def check_whitespace(container, key):
    value = container[key]
    assert value == value.strip(), (f"Invalid {key}: <{value}>", container)


def validate_details(details):
    assert 4 <= len(details) <= 5, details
    assert details["page"] is not None, ("Null page", details)
    assert isinstance(details["page"], int), ("Page isn't a number", details)
    assert details["page"] > 0, ("Invalid page", details)

    def do_validate(attribute):
        check_whitespace(details, attribute)
        assert len(details[attribute]) > 0, ("Empty " + attribute, details)
    if "character" in details:
        do_validate("character")
    for each in ("issue", "publication", "title"):
        assert details[each] is not None
        do_validate(each)

    publication = details["publication"]
    assert publication in ("aku ankan taskukirja", "aku ankka"), publication


def validate(epithet, details):
    assert epithet is not None
    assert epithet == epithet.strip(), "Epithet has blanks: " + epithet
    assert len(epithet) > 0, ("Epithet is empty", details)

    assert details is not None
    for each in details:
        validate_details(each)


def main():
    with open("epithets.json", encoding="utf-8") as filep:
        epithets = json.load(filep)["epithets"]
    for epithet, details in epithets.items():
        validate(epithet, details)


if __name__ == "__main__":
    main()
