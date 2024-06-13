import pygame as pg 

class Sound:
    def __init__(self, game):
        self.game = game 
        pg.mixer.init()
        self.path = 'resources/sound/'
        self.shotgun = pg.mixer.Sound(self.path + 'gun-ethan-sound-2.mp3')
        self.npc_pain = pg.mixer.Sound(self.path + 'caspar-pain.mp3')
        self.npc_death = pg.mixer.Sound(self.path + 'npc_death.wav')
        self.npc_shot = pg.mixer.Sound(self.path + '0216.WAV')
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
        self.theme = pg.mixer.music.load(self.path + 'theme.mp3')
        pg.mixer.music.set_volume(0.3)