from typing import Any, Optional, Dict


class Value:
    def __init__(
        self,
        _Value: Any,
        lifetime: "Lifetime",
        parent_value: Optional["Value"] = None,
        is_parent_value_same_as_Value: bool = False,
    ) -> None:
        if parent_value != None and not isinstance(parent_value, Value):
            raise TypeError("Parent Value is not a Value type")

        self._Value: type(_Value) = _Value
        self.value_buffer: type(_Value) = _Value
        self.child_values: list[Value] = []
        self.changed: bool = False
        self.is_same: bool = False
        self.parent_value: Optional[Value] = None
        self.lifetime = lifetime
        self.lifetime.add_value(self)

        if parent_value != None:
            self.parent_value = parent_value
            if is_parent_value_same_as_Value:
                self.is_same = True
                self._Value = parent_value
            self.parent_value.add_child(Value(self._Value, Lifetime()))

    def take_a_potty(self):
        print(self._Value)

        print(
            self.parent_value
            if self.parent_value == None
            else self.parent_value.get_value()
        )

    def get_value(self):
        if isinstance(self._Value, Value):
            return self._Value._Value
        else:
            return self._Value

    def set_value(self, new_value: Any):
        self.value_buffer = new_value
        self.changed = True
        self.lifetime.refresh_values()

    def add_child(self, child_value: "Value"):
        self.child_values.append(child_value)

    def check_self_or_parent_is_changed(self) -> bool:
        if self.changed:
            return True
        else:
            return False

    def send_new_value_to_children(self, value: "Value"):
        for i in self.child_values:
            # print(f'ummm, this is gonna  be bad but lol, Value: {i.get_value()}')
            i.parent_value = value
            i.changed = True


class Lifetime:
    def __init__(self, Lifetime_name: str = "Main") -> None:
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
