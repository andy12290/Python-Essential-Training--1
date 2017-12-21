
class Animal:
    def talk(self):
        print('Hey I have something to talk')

    def walk(self):
        print('I want to walk here')

class Duck(Animal):
    def quack(self):
        print('Quaaack!')

    def walk(self):
        super().walk()
        print('Walks like a duck.')

class Dog(Animal):
    pass

def main():
    donald = Duck()
    donald.quack()
    donald.walk()
    donald.talk()
    fidoo = Dog()
    print(fidoo.walk())

if __name__ == "__main__": main()
