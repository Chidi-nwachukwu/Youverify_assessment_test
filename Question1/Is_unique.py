def check_unique(data: str):
    for val in data:
        if data.count(val) > 1:
            return False
    return True


if __name__ == "__main__":
    print(check_unique("chid"))
