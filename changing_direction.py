def changing_direction(elements: list[int]) -> int:
    result = 0
    for i in range(len(elements)):
        if i + 1 < len(elements):
            if elements[i] > elements[i+1]:
                flag = 0 # 0 = down | 1 = up
                break
            elif elements[i] < elements[i+1]:
                flag = 1 # 0 = down | 1 = up
                break
            
    for i in range(len(elements)):
        if i + 1 < len(elements):
            if flag == 1 and elements[i] > elements[i+1]:
                flag = 0
                result += 1
            elif flag == 0 and elements[i] < elements[i+1]:
                flag = 1
                result += 1
    return result


print("Example:")

# changing_direction([1, 2, 2, 1, 2, 2])

print(changing_direction([6, 6, 6, 4, 1, 2, 5, 9, 7, 8, 5, 9, 4, 2, 6]))
# print(changing_direction([1, 2, 2, 1, 2, 1, 2]))
# print(changing_direction([1, 2, 2, 1, 2, 2]))

# These "asserts" are used for self-checking
# assert changing_direction([1, 2, 3, 4, 5]) == 0
# assert changing_direction([1, 2, 3, 2, 1]) == 1
# assert changing_direction([1, 2, 2, 1, 2, 2]) == 2
# assert changing_direction([6, 6, 6, 4, 1, 2, 5, 9, 7, 8, 5, 9, 4, 2, 6]) == 7