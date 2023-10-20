from typing import Dict
from ValueClass import Value
from abc import ABC, abstractmethod
from DrawBoz import DrawBoz, BozInstance,TextInstance


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


