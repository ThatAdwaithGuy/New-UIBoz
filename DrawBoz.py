
from functools import lru_cache


class Color:
    
    @staticmethod
    def GetColor(color_code: str) -> str:
        return f"\033[{color_code}m"

    BLACK = GetColor('30')
    RED = GetColor("31")
    GREEN = GetColor("32")
    YELLOW = GetColor("33")
    BLUE = GetColor("34")
    MAGENTA = GetColor("35")
    CYAN = GetColor("36")
    WHITE = GetColor("37")
    
    BG_BLACK = GetColor('40')
    BG_RED = GetColor('41')
    BG_GREEN = GetColor('42')
    BG_YELLOW = GetColor('43')
    BG_BLUE = GetColor('44')
    BG_MAGENTA = GetColor('45')
    BG_CYAN = GetColor('46')
    BG_WHITE = GetColor('47')

    RESET = GetColor("0")




class _Box:
    def __init__(self, Width: int=56):
        self.Width = Width
        StrWidth = "─" * Width
        _Box.UW = f"╭{StrWidth}╮\n"
        _Box.DW = f"╰{StrWidth}╯\n"
    
    ############CHARACTERS############
    URC: str = "╮" # Up Right Conner
    ULC: str = "╭" # Up Left Conner
    DRC: str = "╯" # Down Right Conner
    DLC: str = "╰" # Down Left Conner
    DC: str = "─"  # Dash Character
    UC: str = "│"  # Upward Character
    SPACE:str = " " # Space
    UW: str = "╭────────────────────────────────────────────────────────╮\n" # Upward Wall
    DW: str = "╰────────────────────────────────────────────────────────╯\n" # Upward Wall
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


'''
TODO: 1. Upgrade DrawBoz class so that the Size can be customizable and text placement (center, right, left) ✅
TODO: 2. Make all the customizable ascpects into a array. ✅
TODO: 3. Go to a Psychiatrist and get a brain scan to check how stupid I am ❌
'''

class TextInstance:
    def __init__(self, Text: str, LineNumber: int=6,position: int=1 ,TextColour: str=Color.RESET, TextBackgroundColor: str=Color.RESET) -> None:
        self.Text = Text
        self.LineNumber = LineNumber
        self.position = position
        self.TextColour = TextColour
        self.TextBackgroundColor = TextBackgroundColor
    
    
class DrawBoz:
    def __init__(self, Array: list, Borders: bool=True, Height: int=12, Width: int=56):
        self.Borders: bool = Borders  
        self.Height: int = Height
        self.Width: int = Width  
        self.InputArray: list[list] = Array
        self.CompleteArray: list = ["null"] * self.Height
    
    @staticmethod
    def AddText(TextInstance: TextInstance) -> list: 
        # Extracting Text Instance
        Text = TextInstance.Text 
        LineNumber = TextInstance.LineNumber 
        position = TextInstance.position
        TextColour = TextInstance.TextColour 
        TextBackgroundColor = TextInstance.TextBackgroundColor 

        isColored: bool = True
        text: str = Text
        text = f"{TextColour}{TextBackgroundColor}{text}{Color.RESET}"
        
        if TextColour == Color.RESET and TextBackgroundColor == Color.RESET:
            isColored = False
            
        return [text, LineNumber, position, isColored]
    
    def Update(self, Array: list, Borders: bool=True, Height: int=12, Width: int=56):
        self.Borders = Borders  
        self.Height = Height
        self.Width = Width  
        self.InputArray = Array

    
    @lru_cache(maxsize=128)
    def RenderString(self) -> str:  
        # Just prepares Adds Line data into CompleteArray
        for text, LineNumber, isInverted, isColored in self.InputArray:
            if 0 <= LineNumber < len(self.CompleteArray):
                self.CompleteArray[LineNumber] = [text, LineNumber, isInverted, isColored]
        
        BoxClass: _Box = _Box(self.Width) 
        OutputString: str = "" 
        if self.Borders:
            OutputString += _Box.UW 
        
        for i, v in enumerate(self.CompleteArray): 
            
            if isinstance(v, list) and int(v[2]) > 2:
                
                raise ValueError("Position Value is Invaild, It should be 0 (right), 1 (center) or 2 (left)")
            
            if v == "null" and self.Borders:
                OutputString += _Box.PrintEmptyRow(BoxClass) 

            elif v == "null" and not self.Borders:
                OutputString += "\n"
                
            elif not isinstance(v, list):
                continue    
            
            elif not i == self.CompleteArray.index(v):
                continue
            
            
    
            #*Code to handle Rendering Text
            
            
            if self.Borders:
                if  v[3] == False and v[2] == 0:
                    OutputString += f"{BoxClass.UC} {(v[0])}{'‎' * (self.Width - 6)}{BoxClass.UC}\n"

                elif  v[3] == True and v[2] == 0:
                    OutputString += f"{BoxClass.UC} {(v[0])}{'‎' * (self.Width - 6)}{BoxClass.UC}\n"

                # *Print at Center

                elif  v[3] == False and v[2] == 1:
                    OutputString += f"{BoxClass.UC}{(v[0]).center(self.Width + 12)}{BoxClass.UC}\n"

                elif  v[3] == True and v[2] == 1:
                    OutputString += f"{BoxClass.UC}{(v[0]).center(self.Width + 14)}{BoxClass.UC}\n"

                # *Print at Left Side

                elif  v[3] == False and v[2] == 2:
                    OutputString += f"{BoxClass.UC}{'‎' * (self.Width - 6)}{(v[0])} {BoxClass.UC}\n"

                elif  v[3] == True and v[2] == 2:
                    OutputString += f"{BoxClass.UC}{'‎' * (self.Width - 6)}{(v[0])} {BoxClass.UC}\n"
            
            elif not self.Borders:
                if  v[3] == False and v[2] == 0:
                    OutputString += f"{(v[0])}{'‎' * (self.Width - 6)}\n"

                elif  v[3] == True and v[2] == 0:
                    OutputString += f"{(v[0])}{'‎' * (self.Width - 6)}\n"

                # *Print at Center

                elif  v[3] == False and v[2] == 1:
                    OutputString += f"{(v[0]).center(self.Width + 12)}\n"

                elif  v[3] == True and v[2] == 1:
                    OutputString += f"{(v[0]).center(self.Width + 14)}\n"

                # *Print at Left Side

                elif  v[3] == False and v[2] == 2:
                    OutputString += f"{'‎' * (self.Width - 6)}{(v[0])} \n"

                elif  v[3] == True and v[2] == 2:
                    OutputString += f"{'‎' * (self.Width - 6)}{(v[0])} \n"
            
            
        if self.Borders:
            OutputString += _Box.DW 

        self.RenderString.cache_clear()

        return OutputString
    


