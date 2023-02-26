#!venv/bin/python

import json


def format_main_json():
    with open("epithets.json", encoding="utf-8") as filep:
        data = json.load(filep)
    with open("epithets.json", "w", encoding="utf-8") as filep:
        json.dump(
            data,
            filep,
            ensure_ascii=False,
            sort_keys=True,
            indent=" "*4)


if __name__ == "__main__":
    format_main_json()
