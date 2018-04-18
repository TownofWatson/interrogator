from gtts import gTTS
import pygame

def speak_text(tosay, language):
	tts = gTTS(text=tosay, lang=language, slow=False)
	tts.save("test.mp3")

	pygame.mixer.init()
	pygame.mixer.music.load("test.mp3")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
	    continue

