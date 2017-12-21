
class inclusive_range():
    def __init__(self,*args):
        numargs = len(args)

        if numargs < 1:
            raise TypeError ('Less than 1 args')

        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1

        elif numargs == 2:
            (self.start, self.stop) = args
            self.step = 1

        elif numargs == 3:
            (self.start,self.stop,self.step) = args
        else:
            print('We have more than 3 args')


    def __iter__(self):
        i = self.start
        while(i<self.stop):
            yield i
            i += self.step

def main():
    o = inclusive_range(5,20,2)
    for i in o: print(i, end = ' ')

if __name__ == "__main__": main()
