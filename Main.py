"""
========================= 究極のやるべきことリスト =========================

1. Make a the *last API for the end user
2. Test everything
3. DOCUMENTATION 

* - Probably

====================================================================
"""

from DrawBoz.DrawBoz import DrawBoz, BozInstance, TextInstance, Color
from Utils import HighLevelUtils
from Utils import LowLevelUtils
import time

InputInterface = HighLevelUtils.InputInterface
Value = LowLevelUtils.Value
Lifetime = LowLevelUtils.Lifetime


"""
a = TextInstance("Hello", 6, 0, Color.RESET, Color.RESET, 28).generate_list()
b = TextInstance("Bye", 6, 0, Color.RESET, Color.RESET, 10).generate_list()
Boz = BozInstance([DrawBoz.AddText(a)]).generate_list()
print(DrawBoz(Boz).RenderString())
"""


class Concrete(InputInterface):
    def _ready(self):
        self.life = Lifetime()

        self.a = "Hallo, im Dumb"
        self.b = []
        self.c = []
        self.d = []

    def _update(self):
        self.b = TextInstance(self.a)

        self.c = BozInstance([DrawBoz.AddText(self.b)])

        self.d = DrawBoz(self.c)

        self.a = input("")

        print(self.a)
        print(self.b)
        print(self.c)
        print(self.d.RenderString())
        time.sleep(0.83)
        # print("\033c")


a = Concrete()
a.Run()
