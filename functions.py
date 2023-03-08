import colorama
import sys
import time
import random
import os

reset = colorama.Back.RESET + colorama.Fore.RESET + colorama.Style.RESET_ALL

colors = {
    "red": colorama.Fore.RED,
    "green": colorama.Fore.GREEN,
    "yellow": colorama.Fore.YELLOW,
    "blue": colorama.Fore.BLUE,
    "magenta": colorama.Fore.MAGENTA,
    "cyan": colorama.Fore.CYAN,
    "player": colorama.Fore.LIGHTWHITE_EX + colorama.Style.BRIGHT + reset,
    "white": colorama.Fore.WHITE,
}

def human_say(text: str, speed: int = 150):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/speed)
    print("")


def say(person: dict, text: str, speed: int=150):
    colorama.init()

    if not isinstance(person, dict):
        raise ValueError("Person must be a dictionary\nEXAMPLE: {'name': 'John', 'color': 'red'}")

    if "name" not in person.keys() or "color" not in person.keys():
        raise ValueError("Person must have a name and a color\nEXAMPLE: {'name': 'John', 'color': 'red'}") 

    if person["color"] not in colors.keys():
        raise ValueError(f"Color must be one of these colors: {list(colors.keys())}")
    
    
    print(f"[{colors[person['color']]}{person['name']}{reset}]:", end="")

    human_say(text, speed)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def wait(seconds):
    time.sleep(seconds)

def random_color():
    return random.choice(list(colors.keys()))

def animation(frames: list, fps: int = 24):
    if not isinstance(frames, list):
        raise ValueError("Frames must be a list")

    for frame in frames:
        print(frame)
        time.sleep(1/fps)
        clear()

    time.sleep(1)

def end():
    print(colors["green"] + "Thanks for playing The Game!" + reset)
    wait(1)
    input("Press enter to began a new adventure...")