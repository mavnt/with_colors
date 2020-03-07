from colorama import Back, Fore, Style

from with_colors import *


def with_colors():
    with color(red):
        print("some red text")
        with background(green):
            print("and a green background")
            with style(dim):
                print("and in dim text")
    print("back to normal now")


def colorama():
    print(Fore.RED + "some red text")
    print(Back.GREEN + "and a green background")
    print(Style.DIM + "and in dim text")
    print(Style.RESET_ALL)
    print("back to normal now")


if __name__ == "__main__":
    with_colors()
    colorama()
