import audiolibrary.codec
import audiolibrary.core.audio
import audiolibrary.format

__version__ = '0.1.0'

def read(path: str, format: str = None, codec: str = None) -> audiolibrary.core.audio.Data:
    if format is None:
        format = audiolibrary.format.get_format(path)
    
    if codec is None:
        codec = audiolibrary.codec.get_codec(path, format)

    format = format.upper()
    if format == "AIFF":
        pass #return audiolibrary.core.audio.Data(bit_depth, sample_rate, samples)
    elif format == "AU":
        pass
    elif format == "FLAC":
        pass
    elif format == "MP3":
        pass
    elif format == "OGG":
        pass
    elif format == "WAV":
        pass
    else:
        raise Exception("It is not possible to read the file in this format.")


def write(path: str, format: str, codec: str) -> audiolibrary.core.audio.Data:
    return None
