from typing import Dict
from LowLevelClasses import Value
from abc import ABC, abstractmethod
from DrawBoz import DrawBoz, BozInstance, TextInstance




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


