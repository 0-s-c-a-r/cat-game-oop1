class Cat:
    #The constructor will create a cat for us in code
    #to create a cat, we will need a given name and colour
    #self is the cat that we are creating.
    def __init__(self, given_name, given_colour):
        self.name = given_name
        self.colour= given_colour
        self.age = 1
        self.energy = 50
        self.intelligence = 5
        self.weight = 5


    def train(self):
        print(f"{self.name} is training...")
        self.energy -= 5
        self.intelligence += 1
        self.age += .1

    def feed(self):
        print(f"{self.name} is eating...")
        self.energy += 10
        self.weight += .1
        self.age += .1
    def play(self):
        print(f"{self.name} is playing...")
        self.energy += -10
        self.weight += .1
        self.age += .1

    def sleep(self):
        print(f"{self.name} is slepping...")
        self.energy += 10
        self.intelligence +=-10
        self.age += .1