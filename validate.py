import json


def check_whitespace(container, key):
    value = container[key]
    assert value == value.strip(), (f"Invalid {key}: <{value}>", container)


def validate_details(details):
    assert len(details) == 5, details
    assert details["page"] is not None, ("Null page", details)
    assert isinstance(details["page"], int), ("Page isn't a number", details)
    assert details["page"] > 0, ("Invalid page", details)

    for each in ("character", "issue", "publication", "title"):
        assert details[each] is not None
        check_whitespace(details, each)
        assert len(details[each]) > 0, ("Empty " + each, details)

    assert details["publication"] in ("aku ankan taskukirja", "aku ankka")


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
