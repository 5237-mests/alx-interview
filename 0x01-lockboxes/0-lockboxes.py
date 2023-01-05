#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    to other boxes.
    '''
    numberOfLockedBoxes = len(boxes)
    unlocked_boxes = set([0])
    locked_boxes = set(boxes[0]).difference(set([0]))
    while len(locked_boxes) > 0:
        boxIdx = locked_boxes.pop()
        if not boxIdx or boxIdx >= numberOfLockedBoxes or boxIdx < 0:
            continue
        if boxIdx not in unlocked_boxes:
            locked_boxes = locked_boxes.union(boxes[boxIdx])
            unlocked_boxes.add(boxIdx)
    return numberOfLockedBoxes == len(unlocked_boxes)
