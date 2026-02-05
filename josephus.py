def josephus(int_list, skip):
    skip = skip - 1
    idx = 0
    len_list = len(int_list)
    while len_list > 0:
        idx = (idx + skip) % len_list
        yield int_list.pop(idx)
        len_list -= 1


print(list(josephus([1, 2, 3, 4, 5, 6, 7,8, 9], 3)))