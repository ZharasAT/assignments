def count_in_range(my_list: list, start: int, end: int) -> int:
    ranged_list = [my_list.index(start,end)]
    print(ranged_list)


count_in_range([1, 2, 3, 4, 5, 4, 3, 2, 1], 2, 4) -> 3