from functools import lru_cache
from typing import Any
from dataclasses import dataclass


class Color:
    @staticmethod
    def GetColor(color_code: str) -> str:
        return f"\033[{color_code}m"

    BLACK = GetColor("30")
    RED = GetColor("31")
    GREEN = GetColor("32")
    YELLOW = GetColor("33")
    BLUE = GetColor("34")
    MAGENTA = GetColor("35")
    CYAN = GetColor("36")
    WHITE = GetColor("37")

    BG_BLACK = GetColor("40")
    BG_RED = GetColor("41")
    BG_GREEN = GetColor("42")
    BG_YELLOW = GetColor("43")
    BG_BLUE = GetColor("44")
    BG_MAGENTA = GetColor("45")
    BG_CYAN = GetColor("46")
    BG_WHITE = GetColor("47")

    RESET = GetColor("0")


class _Box:
    def __init__(self, Width: int = 56):
        self.Width = Width
        StrWidth = "─" * Width
        _Box.UW = f"╭{StrWidth}╮\n"
        _Box.DW = f"╰{StrWidth}╯\n"

    ############CHARACTERS############
    URC: str = "╮"  # Up Right Conner
    ULC: str = "╭"  # Up Left Conner
    DRC: str = "╯"  # Down Right Conner
    DLC: str = "╰"  # Down Left Conner
    DC: str = "─"  # Dash Character
    UC: str = "│"  # Upward Character
    SPACE: str = " "  # Space
    UW: str = (
        "╭────────────────────────────────────────────────────────╮\n"  # Upward Wall
    )
    DW: str = (
        "╰────────────────────────────────────────────────────────╯\n"  # Upward Wall
    )
    ##################################

    def PrintEmptyRow(self) -> str:
        return f"{_Box.UC}{_Box.SPACE * self.Width}{_Box.UC}\n"


#           The main idea
#   1. make a array [].  ✅
#   2. then add text into arrays with a function [AddText("Text", line_number, isInverted)].✅
#   3. then using a empty list, add those text into the empty function making
#      the data for the whole box. ✅
#   4. and decode them and make it into a string ready to be printed. ✅

# More TODO: Remove that paradox with the Draw instalization (atlest try) ✅,


"""
TODO: 1. Upgrade DrawBoz class so that the Size can be customizable and text placement (center, right, left) ✅
TODO: 2. Make all the customizable ascpects into a array. ✅
TODO: 3. Go to a Psychiatrist and get a brain scan to check how stupid I am ❌
"""


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


class DrawBoz:
    def __init__(self, BozInstance: BozInstance):
        self.Borders: bool = BozInstance.Borders
        self.Height: int = BozInstance.Height
        self.Width: int = BozInstance.Width
        self.InputArray: list[list[Any]] = BozInstance.Text_data
        self.BufferArrayForColoums: list[list[Any]] = self.InputArray

        self.CompleteArray: list = ["null"] * self.Height

    @staticmethod
    def AddText(TextInstance: TextInstance) -> list:
        # Extracting Text Instance
        Text = TextInstance.Text
        LineNumber = TextInstance.LineNumber
        Coloum = TextInstance.Coloum
        TextColour = TextInstance.TextColor
        TextBackgroundColor = TextInstance.TextBackgroundColor

        isColored: bool = True
        text: str = Text
        text = f"{TextColour}{TextBackgroundColor}{text}{Color.RESET}"

        if TextColour == Color.RESET and TextBackgroundColor == Color.RESET:
            isColored = False

        return [text, LineNumber, Coloum, isColored]

    @staticmethod
    def __get_duplicates(input_array):
        frequency_dict = {}
        for inner_array in input_array:
            second_value = inner_array[1]
            if second_value in frequency_dict:
                frequency_dict[second_value] += 1
            else:
                frequency_dict[second_value] = 1

        # Create a list of the duplicate second values.
        duplicate_second_values = []
        for second_value, frequency in frequency_dict.items():
            if frequency > 1:
                duplicate_second_values.append(second_value)

        # Create an array with another array which has the first, second and third value of the inner input array but only if it has a duplicate second value with any other inner array.
        output_array = []
        for inner_array in input_array:
            second_value = inner_array[1]
            if second_value in duplicate_second_values:
                output_array.append([inner_array[0], second_value, inner_array[2]])

        return output_array

    @lru_cache(maxsize=128)
    def RenderString(self) -> str:
        """This thing holds every line which has two text instances"""

        duplicate_values = self.__get_duplicates(
            [
                (key, value[1], value[2])
                for key, value in {i: v for i, v in enumerate(self.InputArray)}.items()
            ]
        )

        print(duplicate_values)

        ColoumizedInputArray = self.InputArray
        seen_pairs = set()
        for inner_list in self.InputArray:
            pair = (inner_list[1], inner_list[2])
            if pair in seen_pairs:
                raise ValueError(
                    "Error: Duplicate pair at Line Number and Coloum pair."
                )
            seen_pairs.add(pair)

        # Just prepares Adds Line data into CompleteArray
        for text, LineNumber, Coloum, isColored in self.InputArray:
            if 0 <= LineNumber < len(self.CompleteArray):
                self.CompleteArray[LineNumber] = [
                    text,
                    LineNumber,
                    Coloum,
                    isColored,
                ]

        # # Format: [[lineNumber, LineNumber, ...]]
        # same_line_text = [item for item in self.CompleteArray if item != "null"]

        # print(same_line_text)

        BoxClass: _Box = _Box(self.Width)

        OutputString: str = ""

        if self.Borders:
            OutputString += _Box.UW

        # v == null | [Text, LineNumber, Coloum, isColored]
        for i, v in enumerate(self.CompleteArray):
            if v == "null" and self.Borders:
                OutputString += _Box.PrintEmptyRow(BoxClass)

            elif v == "null" and not self.Borders:
                OutputString += "\n"

            elif not isinstance(v, list):
                continue

            elif not i == self.CompleteArray.index(v):
                continue

            elif self.Borders:
                # Is colored
                if v[3]:
                    OutputString += f"{BoxClass.UC} {(v[0])}{'‎' * (self.Width - 5)} {BoxClass.UC}\n"
                elif not v[3]:
                    OutputString += f"{BoxClass.UC} {(v[0])}{'‎' * (self.Width - 5)} {BoxClass.UC}\n"

            elif not self.Borders:
                # Is colored
                if v[3]:
                    OutputString += f"{(v[0])}{'‎' * (self.Width - 6)}\n"
                elif not v[3]:
                    OutputString += f"{(v[0])}{'‎' * (self.Width - 6)}\n"

        if self.Borders:
            OutputString += _Box.DW

        self.RenderString.cache_clear()

        return OutputString


t2 = TextInstance("OMG", Coloum=20)
tb = TextInstance("lol")
ta = TextInstance("byeeee", Coloum=30, LineNumber=3)
te = TextInstance("ba", Coloum=7, LineNumber=3)
tc = TextInstance("baa", Coloum=56, LineNumber=3)
ea = TextInstance("baka", 10)
ah = BozInstance(
    [
        DrawBoz.AddText(t2),
        DrawBoz.AddText(tb),
        DrawBoz.AddText(ta),
        DrawBoz.AddText(te),
        DrawBoz.AddText(tc),
        DrawBoz.AddText(ea),
    ]
)
a = DrawBoz(ah)


a.RenderString()
# print(a.RenderStrin
# g())
