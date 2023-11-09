from ast import Add
from functools import lru_cache

from dataclasses import dataclass

from inspect import currentframe
import re

from typing import Union

from click import STRING


_last_id = 0


def _get_id():
    global _last_id
    _last_id += 1
    return _last_id


@dataclass
class Color:
    BLACK = "\x1b[30m"
    RED = "\x1b[31m"
    GREEN = "\x1b[32m"
    YELLOW = "\x1b[33m"
    BLUE = "\x1b[34m"
    MAGENTA = "\x1b[35m"
    CYAN = "\x1b[36m"
    WHITE = "\x1b[37m"

    BG_BLACK = "\x1b[40m"
    BG_RED = "\x1b[41m"
    BG_GREEN = "\x1b[42m"
    BG_YELLOW = "\x1b[43m"
    BG_BLUE = "\x1b[44m"
    BG_MAGENTA = "\x1b[45m"
    BG_CYAN = "\x1b[46m"
    BG_WHITE = "\x1b[47m"

    RESET = "\x1b[00m"


@dataclass
class Text:
    Text: str
    _id: int
    LineNumber: int = 6
    Column: int = 28
    ForeColor: str = Color.RESET
    BackColor: str = Color.RESET


@dataclass
class BozInstance:
    Text_data: list[Text]
    Borders: bool = True
    Height: int = 12
    Width: int = 56


class DrawBoz:
    def __init__(self, BozInstance: BozInstance) -> None:
        self.Borders: bool = BozInstance.Borders
        self.Height: int = BozInstance.Width
        self.ShowWidth: int = BozInstance.Width
        self.RealWidth: int = BozInstance.Width + 7 * len(BozInstance.Text_data)
        self.InputArray: list[Text] = BozInstance.Text_data

        self.CompleteArray: list = ["null"] * self.Height

    # @staticmethod
    # def AddText(Text: Text) -> Text:
    #    TextData = Text.Text
    #    LineNumber = Text.LineNumber
    #    Column = Text.Coloum
    #    ForeColor = Text.TextColor
    #    BackgroundColor = Text.TextBackgroundColor
    #
    #    return Text(TextData, LineNumber, Column, ForeColor, BackgroundColor)

    @staticmethod
    def _format(string: str, column: int) -> str:
        Space = " " * column
        return Space + string

    @staticmethod
    def _get_duplicates(lst):
        seen_sets = set()
        groups = []
        current_group = []
        for i in lst:
            if i[2] in seen_sets:
                current_group.append(i)
                groups.append(current_group)
                current_group = []
            else:
                seen_sets.add(i[2])
                current_group.append(i)
        return groups

    @staticmethod
    def _overlay_2_strings(string1: str, string2: str):
        smaler_string = ""
        bigger_string = ""
        make_lists_equal_length = lambda list1, list2: (
            list1 + [" "] * (len(list2) - len(list1)),
            list2 + [" "] * (len(list1) - len(list2)),
        )

        if len(string1) > len(string2):
            smaler_string = string1
            bigger_string = string2
            lead_spaces = len(string1)

        elif len(string1) < len(string2):
            smaler_string = string2
            bigger_string = string1
            lead_spaces = len(string2)

        smaler_list = list(smaler_string)
        bigger_list = list(bigger_string)
        output_list = []

        for i in range(len(bigger_list)):
            if bigger_list[i] == " " and smaler_list[i] == " ":
                continue
            elif bigger_list[i] != " " and smaler_list[i] == " ":
                continue
            elif bigger_list[i] == " " and smaler_list[i] != " ":
                continue
            elif bigger_list[i] != " " and smaler_list[i] != " ":
                smaler_list.insert(0, " ")
        smaler_list, bigger_list = make_lists_equal_length(smaler_list, bigger_list)
        for i in range(len(bigger_list)):
            if bigger_list[i] == " " and smaler_list[i] == " ":
                output_list.append(" ")
            elif bigger_list[i] != " " and smaler_list[i] == " ":
                output_list.append(bigger_list[i])
            elif bigger_list[i] == " " and smaler_list[i] != " ":
                output_list.append(smaler_list[i])
        return "".join(output_list)

    def RenderString(self):
        # ================ERROR HANDLING================
        seen_pairs = set()
        for inner_list in self.InputArray:
            pair = (inner_list.LineNumber, inner_list.Column)
            if pair in seen_pairs:
                raise ValueError(
                    "\033[31mERROR\033[0m: Duplicate pair of Line Number and Coloum pair👥."
                )
            seen_pairs.add(pair)

        del seen_pairs

        for i in self.InputArray:
            if i.Column + len(i.Text) + 16 >= self.RealWidth:
                raise ValueError(
                    f"\033[1m\033[31mERROR\033[0m: The Length of the {i.Text} is Leaving The Bounds of The Screen🏃."
                )
        # ==============================================

        # A Beautiful Oneliner to handle Duplicate Values.
        duplicate_values = self._get_duplicates(
            [
                [
                    value.Text,
                    value._id,
                    value.LineNumber,
                    value.Column,
                    value.ForeColor,
                    value.BackColor,
                ]
                for value in {i: v for i, v in enumerate(self.InputArray)}.values()
            ]
        )
        for i in duplicate_values:
            InputListData = []
            current_merge = [self._format(f"{j[4] + j[0] + j[5]}", j[3]) for j in i]

            InputListData.append(
                self._overlay_2_strings(current_merge[0], current_merge[1])
            )
            InputListData.append(i[0][2])

            print(InputListData)
        return duplicate_values


Hallo = DrawBoz(
    BozInstance(
        [
            Text("b", 2, 10, 40),
            Text("Hallo", 1, LineNumber=10, ForeColor=Color.CYAN),
            Text("Gallo", 3, 5, 13),
            Text("Bello", 4, 5),
        ]
    )
)


Hallo.RenderString()
