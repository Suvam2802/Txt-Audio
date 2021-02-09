from gtts import gTTS
import os

text = input("type your text here: ")
language  = 'en'
obj = gTTS(text = text,lang = language,slow = False)
obj.save("sample.mp3")
os.system("sample.mp3")