#!/usr/bin/python3
"""Defines a function that adds all items in a list to a file"""

import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        content = load_from_json_file("add_item.json")
    except FileNotFoundError:
        content = []
    content.extend(sys.argv[1:])
    save_to_json_file(content, "add_item.json")
