#!home/UIBoz/bin/python3.11

""" TODO """
""" ADD COMPONENTS LIKE TEXT BOXES AND BUTTONS WHICH ARE TEXT INSTANCES """
import time
from LowLevelClasses import Value
from DrawBoz import DrawBoz, BozInstance, TextInstance, Color
import keyboard


class Cursor:
    pass


class TextBox:
    def __init__(
        self,
        line_number: int = 6,
        position: int = 1,
        text_color: str = Color.RESET,
        text_background_color: str = Color.RESET,
    ) -> None:
        self.text = ""
        self.is_hovering = True
        self.line_number = line_number
        self.position = position
        self.text_color = text_color
        self.text_background_color = text_background_color

    def get_input(self, event):
        # if event.type ==
        pass

    def get_TextInstance(self):
        return TextInstance(
            self.text,
            self.line_number,
            self.position,
            self.text_color,
            self.text_background_color,
        ).generate_list()


class Button:
    def __init__(
        self,
        line_number: int = 6,
        position: int = 1,
        text_color: str = Color.RESET,
        text_background_color: str = Color.RESET,
    ) -> None:
        self.is_hovering = True

        self.line_number = line_number
        self.position = position
        self.text_color = text_color
        self.text_background_color = text_background_color
        self.is_pressed: bool = False

    def get_is_pressed(self, key_for_activiation: str = "enter"):
        event = keyboard.read_event()
        if (
            event.event_type == keyboard.KEY_DOWN
            and self.is_hovering
            and event.name == key_for_activiation
        ):
            self.is_pressed


class List:
    pass
