def main():

    try:

        fh = open('xlines.txt')
        for line in fh:
            print(line.strip())
    except:
        print('Error in file.')

if __name__ == "__main__":
    main()