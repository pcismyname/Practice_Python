def list_remove(list_1, list_2):
    output = []
    for i in list_1:
        if i not in output and i not in list_2:
            output.append(i)

    return output


def set_remove(set_1, set_2):
    set_1 -= set_2
    return set_1


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

set_a = set(a)
set_b = set(b)

print(list_remove(a, b))
print(set_remove(set_a, set_b))
