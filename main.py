from cat import Cat
import os

print("Welcome to my cat game")
name =  input("whats the name of the cat")
colour = input("enter a cat colour")
myCat = Cat(name, colour)


while True:
    action = input("""
What would you like to do?
1.Train
2.Feed
3.Play
4.Sleep
5.Show stats
""")
    if action == '1':
        myCat.train()
    elif action == '2':
        myCat.feed()
    elif action == '3':
        myCat.play()
    elif action == '4':
        myCat.sleep()
    elif action == '5':
        myCat.stats()

