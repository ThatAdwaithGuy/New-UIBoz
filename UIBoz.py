from DrawBoz import DrawBoz, TextInstance, BozInstance
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
                 _Value,
                 parent_value=None) -> None:
        
        
        
        if parent_value is not None and not isinstance(parent_value, Value):
            raise TypeError('Parent Value is not a Value type')

        self._Value = _Value
        self.value_buffer = _Value
        #self.self_changed = False
        self.child_values: list[Value] = []

        if parent_value != None:
            self.is_parent_changed = False
            self.parent_value = parent_value
            self._Value = parent_value
            self.parent_value.add_child(self)

    ''' For debug purposes ONLY '''
    
    def dump_values(self):
        if isinstance(self._Value, Value):
            print(f"    Value: {self._Value.get_value()}") 
            print('\n')
            print(f"    Value Buffer: {self.value_buffer.get_value()}") 
            print('\n')
            print(f"    child values: {self.child_values}")
            print('\n')
            print(self.parent_value)
            print('\n')
        else:
            print(f" Value: {self._Value}") 
            print('\n')
            print(f" Value Buffer: {self.value_buffer}") 
            print('\n')
            print(f" child values: {self.child_values}")
            print('\n')
            print(self.parent_value)
            print('\n')
    
    ''' <Setters and Getters>'''

    def get_value(self):
        if isinstance(self._Value, Value):
            return self._Value._Value
        else:
            return self._Value
    
    def set_value(self, new_value):
        #if not isinstance(new_value, Value):
        #    raise TypeError('Given Value is not a Value type')
        self.value_buffer = new_value
        self.is_parent_changed = True
        
    
    def add_child(self, child_value):
        if not isinstance(child_value, Value):
            raise TypeError('Given Value is not a Value type')
        self.child_values.append(child_value)

    '''         </>          '''

    ''' this should be in the lifetime loop '''
    def check_self_or_parent_is_changed(self) -> bool:
        if self.is_parent_changed:
            return True
        else:
            return False

    def send_new_value_to_children(self, _Value):
        for i in self.child_values:
            i.parent_value = _Value
            i.is_parent_changed = True



class Lifetime:
    def __init__(self, Lifetime_name: str) -> None:
        self.Lifetime_name = Lifetime_name
        self.value_dict: Dict[int, Value] = {}
    
    def add_value(self, Value: Value):
        id: int = len(self.value_dict) + 1
        self.value_dict[id] = Value
    
    def refresh_values(self):
        for index, value in self.value_dict.items():
            if value.check_self_or_parent_is_changed:
                value._Value = value.value_buffer
                value.send_new_value_to_children(value._Value)
            


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


a: Value = Value('hello')
b: Value = Value('', a)

print(f"B: {b.get_value()}")

life = Lifetime('hello')

life.add_value(a)
life.add_value(b)

a.set_value('hi')

life.refresh_values()

print(f"A: {a.get_value()}")
print(f"B: {b.get_value()}")
b.get_value()

