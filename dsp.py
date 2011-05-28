class DSP:

    def __init__(self,audioFile,chunk):

        self.signal=monoSignal(audioFile,chunk)
        self.chunk=chunk

    def peak(self):
        return self.arr.max

    def hf(self):
        # do hfc on arr and return avg of higher half
        pass

    def lf(self):
        # return avg of lower half
        pass

    def apply(self):
        # todo: apply all analyses on chunk
        return chunk


def monoSignal(audioFile,chunk):
    audioChunk = audio.getpieces(audioFile,[chunk])
    arr = audioChunk.data
    if arr.ndim==2:
        return arr.mean(1)
    return arr


