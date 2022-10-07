from random import random
from gpiozero.tones import Tone
from gpiozero import TonalBuzzer
import random

class c_Music():
    running = True
    def PlaySong(self):
        t = TonalBuzzer("GPIO16")
        while(self.running):
            num = random.randrange(60,79)
            t.play(Tone(midi=num))