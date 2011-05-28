import numpy as np

class DSP:

    def __init__(self,audioFile,chunk):

        self.signal=monoSignal(audioFile,chunk)

        # todo - compute spectrum
        self.chunk=chunk

    def peak(self):
        return self.arr.max

    def hf(self):
        # todo: do hfc on arr and return avg of higher half
        return -1

    def lf(self):
        # todo: return avg of lower half
        return -1

    def apply(self):
        # todo: apply all analyses on chunk
        self.chunk.peak = self.peak()
        self.chunk.hf = self.hf()
        self.chunk.lf = self.lf()
        return self.chunk


def monoSignal(audioFile,chunk):
    audioChunk = audio.getpieces(audioFile,[chunk])
    arr = audioChunk.data
    if arr.ndim==2:
        return arr.mean(1)
    return arr


