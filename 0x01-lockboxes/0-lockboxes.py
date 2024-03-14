#!/usr/bin/python3
"""Solves the lock boxes puzzle """

def find_next_box(boxes, opened):
    """Find the next box to open"""
    for index, box in enumerate(boxes):
        if box and index not in opened:
            return index
    return None

def canUnlockAll(boxes):
    """Check if all boxes can be opened"""
    opened_boxes = set()
    opened_boxes.add(0)
    while True:
        next_box = find_next_box(boxes, opened_boxes)
        if next_box is None:
            return len(opened_boxes) == len(boxes)
        opened_boxes.add(next_box)
        for key in boxes[next_box]:
            if key < len(boxes):
                opened_boxes.add(key)

if __name__ == '__main__':
    main()
