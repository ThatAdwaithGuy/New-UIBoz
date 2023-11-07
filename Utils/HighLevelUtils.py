from typing import Dict
from abc import ABC, abstractmethod


class InputInterface(ABC):
    Running: bool = True

    @abstractmethod
    def _ready(self):
        pass

    @abstractmethod
    def _update(self):
        pass

    def Run(self):
        self._ready()
        while self.Running:
            self._update()


"""
class Page:
    def __init__(self, PageData: BozInstance) -> None:
        self.PageData = PageData
        self.PageDataRendered = DrawBoz(PageData)

    def Refresh(self, NewPageData):
        self.PageData = NewPageData
        self.PageDataRendered = DrawBoz(NewPageData)

    def RenderPage(self) -> str:
        return self.PageDataRendered.RenderString()

    def clear(self) -> None:
        print("\033c")
"""
