def one_array(str1: str, str2: str) -> bool:
    size1 = len(str1)
    size2 = len(str2)

    str1_set = set(str1)
    str2_set = set(str2)

    if size1 > size2:
        if size1 - size2 > 1:
            return False

        if len(str1_set.difference(str2_set)) > 1:
            return False
        return True

    elif size2 > size1:
        if size2 - size1 > 1:
            return False

        if len(str2_set.difference(str1_set)) > 1:
            return False
        return True

    else:
        if len(str2_set.difference(str1_set)) > 1:
            return False
        return True

if __name__ == "__main__":
    print(one_array(str1="ssam", str2="sam"))