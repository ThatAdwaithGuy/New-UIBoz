#!~/UIBoz/bin/python
# import keyboard
from DrawBoz import DrawBoz, BozInstance, TextInstance
import getch


def get_key_pressed():
    a = getch.getch()
    if a not in ["\n"] or a is not None:
        return a


while True:
    a = get_key_pressed()
    if a == "q":
        break
    print(
        DrawBoz(
            BozInstance(
                [DrawBoz.AddText(TextInstance(a).generate_list())]
            ).generate_list()
        ).RenderString()
    )
