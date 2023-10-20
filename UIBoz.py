from rDrawBoz import DrawBoz, TextInstance, BozInstance
import time
from typing import Any, Dict
from typing import Optional
from abc import ABC, abstractmethod

'''
=================================MY IDEA==========================
                            A
                            |
                            B
                            |
                            C
                            |
                            D

                            
A - Text Instance
B - Boz Instance
C - DrawBoz Instance
D - LifeTime
| - A link which if the parent value (A) changes all of its children will get a Refresh notice

Here all of these share a command var, so a if that the value changes then all of them change in a hierarchy 
===================================================================
'''

class Value:
    def __init__(self,
                 _Value: Any,
                 parent_value: Optional['Value'] | None=None,      
                 is_parent_value_same_as_Value: bool=False) -> None:
        


        if parent_value != None and not isinstance(parent_value, Value):
            raise TypeError('Parent Value is not a Value type')
        
        

        self._Value: type(_Value) = _Value
        self.value_buffer: type(_Value) = _Value
        self.child_values: list[Value] = []
        self.changed: bool = False
        self.is_same: bool = False
        self.parent_value: Optional[Value] = None

        if parent_value != None:
            self.parent_value = parent_value
            if is_parent_value_same_as_Value:
                self.is_same = True
                self._Value = parent_value
            self.parent_value.add_child(Value(self._Value))
    
    def take_a_potty(self):

        print(self._Value)
        
        print(self.parent_value if self.parent_value == None else self.parent_value.get_value())
  
  

    

    def get_value(self):
        if isinstance(self._Value, Value):
            return self._Value._Value
        else:
            return self._Value
    
    def set_value(self, new_value: Any):
        self.value_buffer = new_value
        self.changed = True
        
    
    def add_child(self, child_value: 'Value'):
        self.child_values.append(child_value)

    

    def check_self_or_parent_is_changed(self) -> bool:
        if self.changed:
            return True
        else:
            return False

    def send_new_value_to_children(self, value: 'Value'):
        for i in self.child_values:
            #print(f'ummm, this is gonna  be bad but lol, Value: {i.get_value()}')
            i.parent_value = value
            i.changed = True


class InputInterface(ABC):
    Running: bool = True
    @abstractmethod
    def _ready(self):
        pass

    @abstractmethod
    def _update(self):
        pass

    def run(self):
        self._ready()
        while self.Running:
            self._update()

class Lifetime:
    def __init__(self, Lifetime_name: str='Main') -> None:
        self.Running = True
        self.Lifetime_name = Lifetime_name
        self.value_dict: Dict[int, Value] = {}
    
    def add_value(self, Value: Value):
        id: int = len(self.value_dict) + 1
        self.value_dict[id] = Value
    
    def refresh_values(self):
        for index, value in self.value_dict.items():
            if value.changed:
                value.send_new_value_to_children(value.value_buffer)
                value._Value = value.value_buffer
                value.changed = False

                

                
        
class Page:
    def __init__(self, page_data: BozInstance) -> None:
        self.page_data = page_data
        self.page_data_rendered = DrawBoz(page_data)
    
    def refresh(self, new_page_data):
        self.page_data = new_page_data
        self.page_data_rendered = DrawBoz(new_page_data)

    def render_page(self) -> str:
        return self.page_data_rendered.RenderString()

    def clear(self) -> None:
        print('\033c')




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


'''
a = Value('Hallo, im Dumb')
b = Value([], a)
c = Value([], b)
d = Value([], c)

life = Lifetime() 

life.add_value(a)
life.add_value(b)
life.add_value(c)
life.add_value(d)

life.refresh_values()
life.refresh_values()
life.refresh_values()

for i in range(10):


    #print(b.parent_value.get_value())
    b.set_value(TextInstance(b.parent_value.get_value()).generate_list())

    life.refresh_values()
    life.refresh_values()
    life.refresh_values()

    #print(c.parent_value)   
    c.set_value(BozInstance([DrawBoz.AddText(c.parent_value.get_value())]).generate_list())

    life.refresh_values()
    life.refresh_values()
    life.refresh_values()

    #print(d.parent_value)

    d.set_value(DrawBoz(d.parent_value.get_value()))

    life.refresh_values()
    life.refresh_values()
    life.refresh_values()

    a.set_value("Hello, I'm smart")

    life.refresh_values()
    life.refresh_values()
    life.refresh_values()
'''

    
    