import pygame


class Sound:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = sounds = {
    "Sound 1": pygame.mixer.Sound("resources/sound/crash1.ogg"),
    "Sound 2": pygame.mixer.Sound("resources/sound/crash2.mp3")
}
        self.selected_sound = "Sound 1"
    
    def play_sound(self):
        self.sounds[self.selected_sound].play()
    
    def selecte_sound(self, select):
        self.selected_sound = select