from duplicates import without_duplicates


def test_without_duplicates():
    ahmatti = {
        "character": "aku ankka",
        "issue": "501",
        "page": 4,
        "publication": "aku ankan taskukirja",
        "title": "giga-hansu",
    }
    aatelisvaras = {
        "character": "aku ankka",
        "issue": "227",
        "page": 15,
        "publication": "aku ankan taskukirja",
        "title": "tulivuoren uumenissa",
    }
    original = create_epithets({"aatelisvaras": [aatelisvaras], "ahmatti": [ahmatti, ahmatti]})
    expected = create_epithets({"aatelisvaras": [aatelisvaras], "ahmatti": [ahmatti]})
    assert without_duplicates(original) == expected


def create_epithets(epithets):
    return {"epithets": epithets}
