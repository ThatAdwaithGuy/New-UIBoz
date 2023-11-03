class Animation:
    def __init__(self, name: int, width: int, height: int) -> None:
        self.animation_slides = {}
        self.width = width
        self.height = height

    def AddAnimationSlide(self, text: str):
        id_count = len(self.animation_slides) + 1
        self.animation_slides[id_count] = text

    
