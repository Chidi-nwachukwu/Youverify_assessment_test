def urlify(data: str):
    data_list = []
    for d in data:
        if d.isspace():
            data_list.append("%20")
            continue
        data_list.append(d)

    return "".join(data_list)


if __name__ == "__main__":
    result = urlify("mr john smith")
    print(result)
