from gtts import gTTS
import os
tts = gTTS(text="This is the pc speaking", lang='en')
tts.save("pcvoice.mp3")
#os.system("mpg321 good.mp3")