import audiolibrary
import audiolibrary.core.audio
import audiolibrary.codec
import audiolibrary.format
import audiolibrary.format.wav

#print(audiolibrary.format.get_format("tests/resources/audio.wav"))

print(audiolibrary.format.wav.get_info("tests/resources/audio.wav"))