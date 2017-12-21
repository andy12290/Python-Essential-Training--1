def main():
    print('this is the switch.py file')
    a = 0
    b = 1

    while(b<150):

        print(b, end =' ')
        a,b = b, b+a

if __name__ == "__main__": main()
