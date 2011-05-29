import numpy as np
import echonest.audio as audio

CHUNK=256
WINDOW = np.blackman(CHUNK)
class DSP:

    def __init__(self,audioFile,chunk):

        self.signal=monoSignal(audioFile,chunk)

        # todo - compute spectrum
        self.chunk=chunk
        self.calcSpectrum()
        self._centroid=None
        self._spread=None

    def calcSpectrum(self):
        nZeros = CHUNK - self.signal.size % CHUNK
        padded = np.hstack([self.signal, np.zeros(nZeros)])
        # frames are rows
        reshaped = padded.reshape(padded.size/CHUNK,CHUNK)
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

    def spread(self):
        if self._spread:
            return self._spread
        else:
            sum = self.spec.sum()
            self._spread = 0
            centroid = self.centroid()
            for i in range(0,len(self.spec)):
                x=self.spec[i]
                p=x/sum
                self._spread += (x-centroid)**2*p
            return self._spread


    def centroid(self):
        if self._centroid:
            return self._centroid
        else:
            a=0
            for i in range(0,len(self.spec)):
                a=i*self.spec[i]
            self._centroid = a/self.spec.sum()
            return self._centroid

    def kurtosis(self):
        sum = self.spec.sum()
        moment = 0
        centroid = self.centroid()
        for i in range(0,len(self.spec)):
            x=self.spec[i]
            p=x/sum
            moment+=(x-centroid)**4*p
        return moment/(self.spread()**2)

    def peak(self):
        return self.signal.max

    def energy(self):
        return self.spec.sum()

    def halfIndex(self):
        return int(len(self.spec)/2)

    def hf(self):
        i=self.halfIndex()
        hfc=self.hfc()
        return np.sum(hfc[i:])/i

    def lf(self):
        i=self.halfIndex()
        return np.sum(self.spec[:i])/i

    def hfc(self,a=1):
        l=len(self.spec)
        return self.spec*np.linspace(0,l-1,l)**a

    def apply(self):
        # todo: apply all analyses on chunk
        self.chunk.peak = self.peak()
        self.chunk.hf = self.hf()
        self.chunk.lf = self.lf()
        self.chunk.energy = self.energy()
        self.chunk.kurtosis = self.kurtosis()
        return self.chunk

def monoSignal(audioFile,chunk):
    audioChunk = audio.getpieces(audioFile,[chunk])
    arr = audioChunk.data
    if arr.ndim==2:
        return arr.mean(1)
    return arr


