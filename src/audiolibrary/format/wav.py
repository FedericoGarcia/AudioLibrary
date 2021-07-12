import struct
import numpy

# DISCLAIMER: Encodings other than PCM (LPCM) are obsolete, so there is no support in this module.

def get_info(path: str):
    with open(path, "rb", 36) as file:
        header = file.read()
        channels_count = int.from_bytes(header[22:24], "little")
        sample_rate = int.from_bytes(header[24:28], "little")
        bit_depth = int.from_bytes(header[34:36], "little")
    return channels_count, sample_rate, bit_depth