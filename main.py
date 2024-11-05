from cat import Cat
print("Welcome to my cat game")
name =  input("whats the name of the cat")
colour = input("enter a cat colour")
name = Cat(name, colour)
while True:
    action = input("""
What would you like to do?
1.Train
2.Feed
3.Play
4.Sleep
""")
    if action == 1:
        name.train()
    if action == 2:
        name.feed()
    if action == 3:
        name.play()
    if action == 4:
        name.sleep()
    print(name.age, name.energy, name.intelligence, name.weight)