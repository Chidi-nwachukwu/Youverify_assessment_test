


def compress(value):
    compressedString = ""
    index = 0
    len_str = len(value)
    while index != len_str:
        count = 1
        while (index < len_str - 1) and (value[index] == value[index + 1]):
            count += 1
            index += 1
        compressedString += str(value[index]) + str(count)
        index = index + 1

    if len(compressedString) > len(value):
        return value
    else:
        return compressedString




if __name__ == "__main__":
    print(compress("aaccccccaaa"))

