#!/usr/bin/python3
"""
Determines if all given boxes can be opened
"""


def FindKeys(keys, l_box, keys_found):
    """
    Return keys found from all boxes
    """
    if not l_box:
        return keys_found
    for k in keys:
        if k not in keys_found:
            keys_found.append(k)
            FindKeys(l_box[k], l_box, keys_found)
    return keys_found


def canUnlockAll(boxes):
    """
    Return True if all boxes can be opened, else return False
    """
    if (type(boxes) is not list) or (len(boxes) == 0):
        return False
    lockboxes = {}
    for i in range(len(boxes)):
        lockboxes[i] = boxes[i]
    keys = boxes[0]
    keys_found = FindKeys(keys, lockboxes, [])
    lockboxes.pop(0)
    for i in keys_found:
        lockboxes.pop(i, None)
    return not lockboxes
