import numpy
import audiolibrary.core.audio
import audiolibrary.codec

def decode(Data = audiolibrary.codec.Data) -> audiolibrary.core.audio.Data:
    audio_file = None #decode_file(audio_file_path)
    pcm_samples = audio_file.samples
    bit_depth = 16
    sample_rate = 44100
    channels_count = audio_file.nchannels
    channel_samples_count = audio_file.num_frames
    total_samples_count = channels_count * channel_samples_count

    samples = numpy.zeros(shape = (channels_count, channel_samples_count))

    for sample in range(total_samples_count):
        samples[sample % channels_count][numpy.floor(sample / channels_count)] = pcm_samples[sample]

    return audiolibrary.core.audio.Data(bit_depth, sample_rate, samples)

def encode(Data = audiolibrary.core.audio.Data) -> audiolibrary.codec.Data:
    return None