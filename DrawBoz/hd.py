import os
import getch


def GetKeyPressed():
    a = getch.getch()
    if a not in ["\n"] or a is not None:
        return a


while True:
    print("\033c")
    print(GetKeyPressed())
