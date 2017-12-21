

class Egg():

    def __init__(self, kind):
        self.kind = kind

    def whatkind(self):
        return self.kind


def main():
    f = Egg('fried')
    print(f.whatkind())



if __name__ == '__main__':
    main()