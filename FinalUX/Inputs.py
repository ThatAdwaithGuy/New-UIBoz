#!~/UIBoz/bin/python
# import keyboard
from DrawBoz.DrawBoz import DrawBoz, BozInstance, TextInstance
import getch  # typ: ignore


def get_key_pressed():
    a = getch.getch()
    if a not in ["\n"] or a is not None:
        return a
