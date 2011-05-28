import numpy as np

CHUNK=256
WINDOW = np.blackman(CHUNK)
class DSP:

    def __init__(self,audioFile,chunk):

        self.signal=monoSignal(audioFile,chunk)

        # todo - compute spectrum
        self.chunk=chunk

    def spectrum(self):
        nZeros = CHUNK - self.signal.size % CHUNK
        padded = np.hstack([self.signal, np.zeros(nZeros)])
        # frames are rows
        reshaped = padded.reshape(CHUNK,padded.size/CHUNK)
        # apply window to each frame
        reshaped = np.apply_along_axis(lambda x: x*WINDOW, 1, reshaped)
        # do fft on each row
        S = np.fft.rfft(reshaped)
        # get power spectrum
        SPow = abs(S)**2
        # calc mean for each bucket - 0 is column axis
        self.spec = SPow.mean(0)
        # remove DC offset
        self.spec[0]==0

    def peak(self):
        return self.arr.max

    def halfIndex(self):
        return int(len(self.spec)/2)


    def hf(self):
        # todo: do hfc on arr and return avg of higher half
        return np.sum(self.spec[halfIndex():])/halfIndex()

    def lf(self):
        # todo: return avg of lower half
        return np.sum(self.spec[:halfIndex()])/halfIndex()

    def apply(self):
        # todo: apply all analyses on chunk
        self.chunk.peak = self.peak()
        self.chunk.hf = self.hf()
        self.chunk.lf = self.lf()
        return self.chunk

    def hfc(self,a=1):
        l=len(self.spec)
        return self.spec*linspace(0,l-1,l)**a

def monoSignal(audioFile,chunk):
    audioChunk = audio.getpieces(audioFile,[chunk])
    arr = audioChunk.data
    if arr.ndim==2:
        return arr.mean(1)
    return arr


