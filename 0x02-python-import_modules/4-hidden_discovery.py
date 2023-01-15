#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    dir_arr = dir(hidden_4)

    for i in dir_arr:
        if not i.startswith('__'):
            print("{:s}".format(i))
