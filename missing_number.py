def missing_number(items: list[int]) -> int:
    n = len(items)
    items.sort()
    s = (items[-1] - items[0]) // n

    for i in range(n):
        item = items[i] + s
        if items[i+1] != item:
            return item
    return 0


print("Example:")
# missing_number([1, 4, 2, 5])
print(missing_number([1, 4, 2, 5]))

# These "asserts" are used for self-checking
# assert missing_number([1, 4, 2, 5]) == 3
# assert missing_number([2, 6, 8]) == 4