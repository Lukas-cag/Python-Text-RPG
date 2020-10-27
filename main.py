#external
import random
import time

#local
import items
import player

def Start():
    print("TEXT ADVENTURE - (c) Lukas c 2020")
    print("What is your name?")
    player.name = input(">>> ")
    print("Hello " + player.name + ", starting game...")

def forestRuinsOutside():
    print("You are in a forest, ahead of you a temple is buried half in the dirt.\nIt is covered in vines which seem to have blocked the entrance")
    time.sleep(1)
    print("There is a cliff to your left that looks unscalable,\nto your right is a river")
    time.sleep(1)
    print("What do you do? \nHINT:\ntry commands like: go to: , inspect: etc\nOpen your inventory with 'inv'")
    option = input(">>> ")


Start()
time.sleep(1)
forestRuinsOutside()
    