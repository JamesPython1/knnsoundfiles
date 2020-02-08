# Author: James Grace
# Date: 02.02.2020
# Version: 1
# Title: record script

import pyaudio, wave

class audioRec():
	def __init__(self):
		self.FORMAT = pyaudio.paInt16
		self.CHANNELS = 2
		self.RATE = 44100
		self.CHUNK = 1024
	def record_audio(self,RECORD_SECONDS,WAVE_OUTPUT_FILENAME):
		self.audio = pyaudio.PyAudio()
		self.stream = self.audio.open(format=self.FORMAT,
									  channels=self.CHANNELS,
									  rate=self.RATE, input=True,
									  frames_per_buffer=self.CHUNK)
		print("Listening ... ")
		self.frames=[]
		for count in range(int(self.RATE / self.CHUNK * RECORD_SECONDS)):
			self.data = self.stream.read(self.CHUNK)
			self.frames.append(self.data)
		print("RECORDING OVER")

		self.stream.stop_stream()
		self.stream.close()
		self.audio.terminate()

		#save audio
		self.waveFile = wave.open(WAVE_OUTPUT_FILENAME, "wb")
		self.waveFile.setnchannels(self.CHANNELS)
		self.waveFile.setsampwidth(self.audio.get_sample_size(self.FORMAT))
		self.waveFile.setframerate(self.RATE)
		self.waveFile.writeframes(b''.join(self.frames))
		self.waveFile.close()

r = audioRec()
hg=input("Hello or goodbye: ")
i=1
while True:
	option = int(input("1 or 0: "))
	if option == 0:
		break
	print("recording ... ")
	r.record_audio(3,hg+str(i)+".wav")
	i=i+1



