from functools import lru_cache
from typing import Any
from dataclasses import dataclass


@dataclass
class Color:
    @staticmethod
    def GetColor(color_code: str) -> str:
        return f"\033[{color_code}m"

    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    RESET = "\033[0m"
    BLANK = ""


@dataclass
class TextInstance:
    Text: str
    LineNumber: int = 6
    Coloum: int = 28
    TextColor: str = Color.RESET
    TextBackgroundColor: str = Color.RESET


@dataclass
class BozInstance:
    Text_data: list[list[Any]]
    Borders: bool = True
    Height: int = 12
    Width: int = 56


@dataclass
class Text:
    Text: str
    LineNumber: int = 6
    Column: int = 28
    ForeColor: str = Color.BLANK
    BackColor: str = Color.BLANK


class DrawBoz:
    def __init__(self, BozInstance: BozInstance) -> None:
        self.Borders: bool = BozInstance.Borders
        self.Height: int = BozInstance.Height
        self.Width: int = BozInstance.Width
        self.InputArray: list[list[Any]] = BozInstance.Text_data
        self.BufferArrayForColoums: list[list[Any]] = self.InputArray

        self.CompleteArray: list = ["null"] * self.Height

    @staticmethod
    def AddText(TextInstance: TextInstance) -> Text:
        TextData = TextInstance.Text
        LineNumber = TextInstance.LineNumber
        Column = TextInstance.Coloum
        ForeColor = TextInstance.TextColor
        BackgroundColor = TextInstance.TextBackgroundColor

        return Text(TextData, LineNumber, Column, ForeColor, BackgroundColor)

    def RenderString(self) -> str:
        ...
