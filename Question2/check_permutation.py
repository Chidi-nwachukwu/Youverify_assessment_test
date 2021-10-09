def check_permutation(data: str, data2: str) -> bool:
    if len(data) != len(data2):

        return False
    str1 = "".join(sorted(data))
    str2 = "".join(sorted(data2))

    for index in range(len(data)):
        if str1[index] != str2[index]:
            return False
        return True

if __name__ == "__main__":
    print(check_permutation(data="chidi", data2="chima"))