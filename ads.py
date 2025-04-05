import sys
import time
import random

def type(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def types(text, delay=0.4):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def model():
    choice = input("> ")

    if choice==("S"):
        print("PURCHASE COMPLETE")
        type(" -$200")

    if choice==("M"):
        print("PURCHASE COMPLETE")
        type(" -$299.99")

    if choice==("L"):
        print("PURCHASE COMPLETE")
        type(" -$499.99")

    elif choice==("XL"):
        print("OUT OF STOCK FOR XL")
        type(" -$0")

def printer():
    printerchoice = input("what would you like to print? > ")
    types(f"{printerchoice}")

def slow():
    slowness = input(" > ")
    types(f"{slowness}")

def medium():
    mediumness = input(" > ")
    type(f"{mediumness}")

def instant():
    insta = input(" > ")
    print(f"{insta}")

def one():
    type("BUY NEW COOL CARCAR, STARTING AT ONLY $200")
    time.sleep(2)
    choice = input("click ad? y/n > ")

    if choice==("y"):
        print("CARCAR \n \n")
        print("SELECT MODEL - S M L")
        model()

def two():
    type("ANTVIRUS ANTIVIRUS, WE STAND WITH THE ANTS AND USE ANT POWER TO FIGHT OFF THE VIRUSES")
    time.sleep(2)
    choice = input("click ad? y/n > ")

    if choice==("y"):
        print("DOWNLOADING/UPDATING")
        types("...")
        print("DONE!")

def three():
    type("WILL PRINT WHATEVER YOU WANT")
    time.sleep(2)
    choice = input("click ad? y/n > ")

    if choice==("y"):
        printer()

def four():
    type("will print anything you want at any speed, also you HAVE to print something lol")
    choice = input("Select speed: Slow, Medium, Insta-Print")
    
    if choice==("Slow"):
        slow()

    if choice==("Medium"):
        medium()

    elif choice==("Insta-Print"):
        instant()
def random_function():
    func_list = [one, two, three, four]
    random.shuffle(func_list)
    return func_list

busy = False
function_order = random_function()

while True:
    if not busy:
        busy = True
        current_func = function_order.pop(0)
        current_func()
        if len(function_order) == 0:
            function_order = random_function()
        time.sleep(5)
        busy = False
    else:
        time.sleep(1)
