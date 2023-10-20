from typing import Any, Optional



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

