def main():
    testfunc(1,2,3,4,5,5)

def testfunc(one, two, three, *args):
    print(one, two, three)

    print('This is a test function')

if __name__ == "__main__":
    main()