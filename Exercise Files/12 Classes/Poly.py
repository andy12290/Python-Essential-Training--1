class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')


class Dog:

    def bark(self):
        print('Woof')

    def fur(self):
        print('The dog has fur')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    moti = Dog()
    moti.bark()
    moti.fur()

if __name__ == "__main__": main()
