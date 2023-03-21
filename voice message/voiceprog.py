from gtts import gTTS
pajery = "As far as I concered"
language= 'en'
bmx=gTTS(text=pajery, lang=language, slow=False)
bmx.save("audio1.mp3")