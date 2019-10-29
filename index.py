the_Array = [15,22,84,14,88,23]


def min_max_difference(theList):
    theMaxValue = max(theList)
    theMinValue = min(theList)
    return theMaxValue - theMinValue

print(min_max_difference(the_Array))

