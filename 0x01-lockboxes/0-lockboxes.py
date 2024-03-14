#!/usr/bin/python3
'''A module for lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    num = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        box_id = unseen_boxes.pop()
        if not box_id or box_id >= num or box_id < 0:
            continue
        if box_id not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[box_id])
            seen_boxes.add(box_id)
    return num == len(seen_boxes)
