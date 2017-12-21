def main():
    print("This is the functions.py file.")
    for i in inclusive_range(23):
        print(i, end = ' ')


# Lets start with the arguments.
def inclusive_range (*args):

    numargs = len(args)

    if numargs < 1:
        raise TypeError('Atleast we need one args')

    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1

    elif numargs == 2:
        stop = args
        start = args
        step = 1

    elif numargs == 3:

        star, stop, step = args

    else:
        raise TypeError('More than one args')

    i = start

    while(i < stop):
         yield i
         i += step


if __name__ == "__main__":
    main()
