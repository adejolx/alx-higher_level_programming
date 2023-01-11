def convert_to_list(is_tuple):
    new_list = list(is_tuple)
    return new_list


def convert_to_tuple(is_list):
    new_tuple = tuple(is_list)
    return new_tuple


def fill_empty_space(list_x):
    if (not list_x):
        list_x.append(0)
        list_x.append(0)
    return list_x


def cap_at_two(list_x):
    return list_x[:2]


def adjust_length(list_x):
    if (len(list_x) < 2):
        return fill_empty_space(list_x)
    if (len(list_x) > 2):
        return cap_at_two(list_x)
    return list_x


def add_tuple(tuple_a=(), tuple_b=()):
    new_list_a = adjust_length(convert_to_list(tuple_a))
    new_list_b = adjust_length(convert_to_list(tuple_b))
    list_ab = [new_list_a[i] + new_list_b[i] for i in range(2)]

    return convert_to_tuple(list_ab)
