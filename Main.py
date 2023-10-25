from DrawBoz import DrawBoz, TextInstance, BozInstance
from LowLevelClasses import Value, Lifetime
from HighLevelClasses import InputInterface
import time
from pynput import keyboard

"""
========================= 究極のやるべきことリスト =========================

1. Make a the *last API for the end user
2. Test everything
3. DOCUMENTATION 

* - Probably

====================================================================
"""


def keyboard_input(key):
    print(str(key))
    with open("key.txt", "a") as keyLog:
        char = key.char
        keyLog.write(char)


a = keyboard.Listener(on_press=keyboard_input)
a.start()
input()


"""
class Concrete(InputInterface):
    def _ready(self):
        
        self.life = Lifetime() 

        self.a = Value('Hallo, im Dumb', self.life)
        self.b = Value([], self.life, self.a)
        self.c = Value([], self.life, self.b)
        self.d = Value([], self.life, self.c)

    def _update(self):
        
        self.b.set_value(TextInstance(self.b.parent_value.get_value()).generate_list())


        self.c.set_value(BozInstance([DrawBoz.AddText(self.c.parent_value.get_value())]).generate_list())


        self.d.set_value(DrawBoz(self.d.parent_value.get_value()))

        
        self.a.set_value('byee')

        
        print(self.d.get_value().RenderString())
        time.sleep(0.83)
        print('\033c')

a = Concrete()
a.run()
"""
