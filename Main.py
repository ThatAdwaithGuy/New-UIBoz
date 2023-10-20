from DrawBoz import DrawBoz, TextInstance, BozInstance
from ValueClass import Value
from LifetimeClasses import InputInterface, Lifetime

'''
========================= 究極のやるべきことリスト =========================

1. Make a the *last API for the end user
2. Test everything
3. DOCUMENTATION 

* - Probably

====================================================================
'''






class Concrete(InputInterface):
    def _ready(self):
        self.a = Value('Hallo, im Dumb')
        self.b = Value([], self.a)
        self.c = Value([], self.b)
        self.d = Value([], self.c)

        self.life = Lifetime() 

        self.life.add_value(self.a)
        self.life.add_value(self.b)
        self.life.add_value(self.c)
        self.life.add_value(self.d)

    def _update(self):
        #print(b.parent_value.get_value())
        self.b.set_value(TextInstance(self.b.parent_value.get_value()).generate_list())

        self.life.refresh_values()
        self.life.refresh_values()
        self.life.refresh_values()

        #print(c.parent_value)   
        self.c.set_value(BozInstance([DrawBoz.AddText(self.c.parent_value.get_value())]).generate_list())

        self.life.refresh_values()
        self.life.refresh_values()
        self.life.refresh_values()

        #print(d.parent_value)

        self.d.set_value(DrawBoz(self.d.parent_value.get_value()))

        self.life.refresh_values()
        self.life.refresh_values()
        self.life.refresh_values()

        self.a.set_value("Hello, I'm smart")

        self.life.refresh_values()
        self.life.refresh_values()
        self.life.refresh_values()
        print(self.d.get_value().RenderString())

a = Concrete()
a.run()




    
    