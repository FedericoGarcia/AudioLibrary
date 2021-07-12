import numpy

class RawData:
    def __init__(self, bit_depth: int, sample_rate: int, data: numpy.ndarray) -> None:
        pass

class Data:
    def __init__(self, bit_depth: int, sample_rate: int, samples: numpy.ndarray) -> None:
        self.__bit_depth = bit_depth
        self.__sample_rate = sample_rate
        self.__samples = samples

    @property
    def bit_depth(self) -> int:
        return self.__bit_depth

    @property
    def sample_rate(self) -> int:
        return self.__sample_rate

    @property
    def samples(self) -> numpy.ndarray:
        return self.__samples

    @property
    def channels_count(self) -> int:
        return self.samples.shape[0]

    @property
    def channel_samples_count(self) -> int:
        return self.samples.shape[1]

    @property
    def total_samples_count(self) -> int:
        return self.channels_count * self.channel_samples_count

    @property
    def duration(self) -> float:
        return self.channel_samples_count / self.sample_rate

    @property
    def size(self) -> float:
        return self.bit_depth * self.total_samples_count / 8