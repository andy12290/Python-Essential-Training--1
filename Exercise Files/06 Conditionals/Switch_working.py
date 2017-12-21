

# switch case statment.

def main():
    print('this is the switch.py file')

    choices = dict(one='first',
     two='two',
     three='three'
     )

    v = 'one'
    print(choices.get(v, 'other'))

if __name__ == "__main__":
    main()
