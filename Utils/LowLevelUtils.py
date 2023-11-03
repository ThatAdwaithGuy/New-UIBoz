from typing import Any, Optional, Dict


class Value:
    def __init__(
        self,
        value: Any,
        lifetime: "Lifetime",
        ParentValue: Optional["Value"] = None,
        IsParentValueSameAsValue: bool = False,
    ) -> None:
        if ParentValue != None and not isinstance(ParentValue, value):
            raise TypeError("Parent Value is not a Value type")

        self.value: type(value) = value
        self.ValueBuffer: type(value) = value
        self.ChildValues: list[value] = []
        self.changed: bool = False
        self.IsSame: bool = False
        self.ParentValue: Optional[value] = None
        self.lifetime = lifetime
        self.lifetime.add_value(self)

        if ParentValue != None:
            self.ParentValue = ParentValue
            if IsParentValueSameAsValue:
                self.IsSame = True
                self.value = ParentValue
            self.ParentValue.AddChild(Value(self.value, lifetime()))

    
    def GetValue(self):
        if isinstance(self.value, Value):
            return self.value.value
        else:
            return self.value

    def SetValue(self, NewValue: Any):
        self.ValueBuffer = NewValue
        self.changed = True
        self.lifetime.Refresh()

    def AddChild(self, child_value: "Value"):
        self.ChildValues.append(child_value)


    def SendNewValueToChildren(self, value: "Value"):
        for i in self.ChildValues:
            # print(f'ummm, this is gonna  be bad but lol, Value: {i.get_value()}')
            i.ParentValue = value
            i.changed = True


class Lifetime:
    def __init__(self, Lifetime_name: str = "Main") -> None:
        self.Running = True
        self.Lifetime_name = Lifetime_name
        self.value_dict: Dict[int, Value] = {}

    def add_value(self, Value: Value):
        id: int = len(self.value_dict) + 1
        self.value_dict[id] = Value

    def Refresh(self):
        for index, value in self.value_dict.items():
            if value.changed:
                value.SendNewValueToChildren(value.ValueBuffer)
                value.value = value.ValueBuffer
                value.changed = False
