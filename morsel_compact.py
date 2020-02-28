

def compact(some_iterable):
    """Accept a sequence (e.g. list) that returns a new iterable with ADJACENT duplicate values removed.
       Making use of Python's set, we remove duplicates and create a new list.  We lose the original order of the
       sequence.
    """
    unique = set(some_iterable)
    compacted_list = [item for item in unique]

    # return an iterable, not just a list
    return iter(compacted_list)


def solution_compact(sequence):
    """Solution from Python morsels
    Return new iterable with adjacent duplicate values removed."""

    deduped = []

    # Always appending item 0, the first item in the sequence.
    # subsequent items are appended if they are not equal to the item
    # corresponding to the previous index
    for i, item in enumerate(sequence):
        if i == 0 or item !=sequence[i-1]:
            deduped.append(item)
    return deduped

def second_solution_compact(sequence):
    """Return new iterable with adjacent duplicate values removed.  This time employ the use of
       Python's zip function.
    """
    deduped = []
    # zip became available in Python 3.5
    # Zip together the original sequence, against another sequence which is just
    # the original sequence shifted by one: [object(), *sequence]
    # the * is unpacking each of the items in the sequence into a new list, after the object().
    # object() is the first item in a second list because a new object will not be compared as equal to any of
    # the items in sequence (each objet is only equal to itself by default)
    # Trey prefers the first solution above, which employs the index-based solution.  I do too, although
    # the item != previous is more obvious than if i ==0 or item != sequence[i-1].  However,
    # the syntax for creating a new sequence with offset of one object isn't intuitively obvious.  But it is
    # a clever use of the zip function.

    for item, previous in zip(sequence, [object(), *sequence]):
        if item != previous:
            deduped.append(item)
    return deduped

if __name__ == "__main__":
    some_list = ['z','xyz','a','a','aaa']
    compact_list = compact(some_list)
    print(f'Compacted list: {list(compact_list)}')

    # Bonus 1
    print("\n\nBonus 1\n========\n")
    compact_list = compact(n**2 for n in [1,2,2])
    print(f'Compacted list: {list(compact_list)}')

    # print("\n\nFirst Solution Bonus 1 \n=======================\n")
    # compact_list = solution_compact(n ** 2 for n in [1, 2, 2])
    # print(f"First Solution's Compacted list: {list(compact_list)}")

    # Bonus 2
    print("\n\nBonus 2\n========\n")
    print("Is the compacted list an iterable? ", iter(compact_list) is compact_list)

    # Test out the official solution
    compact_list = solution_compact(some_list)
    print(f"\n\nSolution's Compacted list: {list(compact_list)}")
    print("Is the compacted list an iterable? ", iter(compact_list) is compact_list)

    # Test out the second official solution
    compact_list = second_solution_compact(some_list)
    print(f"\n\nSecond Solution's Compacted list: {list(compact_list)}")
    print("Is the compacted list an iterable? ", iter(compact_list) is compact_list)