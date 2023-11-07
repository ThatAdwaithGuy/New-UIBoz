from typing import Dict


class Animation:
    def __init__(self, name: str, width: int = 1, height: int = 1) -> None:
        self.animation_slides: Dict[int, str] = {}
        self.width = width
        self.height = height
        self.CurrentSlide = 0
        self.is_running = False

    def AddAnimationSlide(self, text):
        id_count = len(self.animation_slides) + 1
        self.animation_slides[id_count] = text

    def DisplayAnimation(self):
        ...

    def RefreshAnimation(self):
        ...
