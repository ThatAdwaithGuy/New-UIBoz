from rDrawBoz import DrawBoz, TextInstance, BozInstance
import time
from typing import Any, Dict

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
                 parent_value: 'Value'=None,
                 
                 is_parent_value_same_as_Value: bool=False) -> None:
        

        ''' Type hinting '''
        if parent_value != None and not isinstance(parent_value, Value):
            raise TypeError('Parent Value is not a Value type')
        
        

        self._Value: type(_Value) = _Value
        self.value_buffer: type(_Value) = _Value
        self.child_values: list[Value] = []
        self.changed = False
        self.is_child = False
        self.is_same = False

        if parent_value != None:
            self.parent_value = parent_value
            if is_parent_value_same_as_Value:
                self.is_same = True
                self._Value = parent_value
            self.parent_value.add_child(self)

    ''' <Setters and Getters>'''

    def get_value(self):
        if isinstance(self._Value, Value):
            return self._Value._Value
        else:
            return self._Value
    
    def set_value(self, new_value: Any):
        
        self.value_buffer = new_value
        self.changed = True
        
    ''' child_value is Value Type '''
    def add_child(self, child_value: 'Value'):
        
        self.child_values.append(child_value)

    '''         </>          '''

    ''' this should be in the lifetime loop '''
    def check_self_or_parent_is_changed(self) -> bool:
        if self.changed:
            return True
        else:
            return False

    def send_new_value_to_children(self, _Value: 'Value'):
        for i in self.child_values:
            #print(f'ummm, this is gonna  be bad but lol, Value: {i.get_value()}')
            i.parent_value = _Value
            i.changed = True



''' overide both of these in the child class '''
'''
    Like this

    class ExampleClass(InputFunctions):
        def __init__(self):
            self.super()
        @overide
        def _ready(self):
            ...
        def _update(self):
            ...
        
'''

class InputFunctions:
    def __init__(self) -> None:
        pass
        
    def _ready(self):
        pass

    def _update(self):
        pass
    
    ''' Run Both of these ^ '''
    def Run(self):
        self._ready()
        while True:
            self._update()
            self.refresh_values()
    

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
            if not value.check_self_or_parent_is_changed():
                continue

            if value.is_same:
                value.send_new_value_to_children(value.value_buffer)
                value._Value = value.parent_value
            else:
                value.send_new_value_to_children(value.value_buffer)
                value._Value = value.value_buffer

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

class MyFunctions(InputFunctions):
    def __init__(self) -> None:
        Running = True
    
    
    def _ready(self):
        self.a = Value('Hello')
        self.b = Value([], self.a)
        self.c = Value([], self.b)
        self.d = Value([], self.c)
        self.life = Lifetime() 
        self.life.add_value(self.a)
        self.life.add_value(self.b)
        self.life.add_value(self.c)
        self.life.add_value(self.d)

    def _update(self):
        self.b.set_value(TextInstance(self.a.get_value()))
        self.c.set_value(BozInstance([DrawBoz.AddText(self.c.parent_value.get_value())]))
        self.d.set_value(DrawBoz(self.d.parent_value))

        print(self.d.get_value)


a = MyFunctions()
a.Run()