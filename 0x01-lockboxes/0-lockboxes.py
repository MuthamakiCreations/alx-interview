#!/usr/bin/python3
"""Module that finds out if all lockboxes can be opened"""


def canUnlockAll(boxes):
    if not boxes:
        return False
    box_len = len(boxes)
    open_box = [0]

    for key in open_box:
        for box in boxes[key]:
            if box not in open_box and box < box_len:
                open_box.append(box)

    if len(open_box) == box_len:
        return True
    return False
