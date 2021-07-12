'''
class Endian:
    BIG = 0
    LITTLE = 1

def endianness(endian: bool, data: bytes) -> bytes: # Default input is in big endian
    if endian == Endian.LITTLE:
        return data[::-1]
    elif endian == Endian.BIG:
        return data
    else:
        return None
'''

def get_format(path: str) -> str:
    with open(path, 'rb', 16) as file: # Read in binary, first 16 bytes
        head = file.read()
        if head[0:2] == b'\xFF\xF1' or head[0:2] == b'\xFF\xF9':
            return "AAC"
        elif head[0:4] == b'\x46\x4F\x52\x4D' and head[8:12] == b'\x41\x49\x46\x46':
            return "AIFF"
        elif head == b'\x30\x26\xB2\x75\x8E\x66\xCF\x11\xA6\xD9\x00\xAA\x00\x62\xCE\x6C':
            return "WMA"
        elif head[0:4] == b'\x2E\x73\x6E\x64':
            return "AU"
        elif head[0:4] == b'\x66\x4C\x61\x43':
            return "FLAC"
        elif head[0:2] == b'\xFF\xF2' or head[0:2] == b'\xFF\xF3' or head[0:2] == b'\xFF\xFB':
            return "MP3"
        elif head[0:3] == b'\x49\x44\x33':
            return "MP3"
        elif head[0:4] == b'\x4F\x67\x67\x53':
            return "OGG"
        elif head[0:4] == b'\x52\x49\x46\x46' and head[8:12] == b'\x57\x41\x56\x45':
            return "WAV"
        else:
            return None