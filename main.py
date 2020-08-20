from music21 import *
from pylab import *
import matplotlib.pyplot as plt

environment.set("musicxmlPath", "C:/Program Files/MuseScore 3/bin/MusesCore3.exe")

#definindo as funcoes
#funcao seno
def discrete_sin(theta, low_note, high_note):
    return high_note + int(high_note - low_note) * sin(theta)

#funcao afim
def discrete_afim(parametro, low_note, high_note):
    return int((high_note-low_note) * 0.3 * parametro)

#funcao quadratica
def discrete_quad(parametro, low_note, high_note):
    return int(parametro ** 2)

#funcao exponencial
def discrete_exp(parametro, low_note, high_note):
    return 0.05 * int(2 ** parametro)

stream = stream.Stream()

pitchesList = [discrete_quad(n, 60, 72) for n in range(-12,12)]
print(pitchesList)
#plt.plot(pitchesList)
#plt.show()

[stream.append(note.Note(midi = pitch)) for pitch in pitchesList]

stream.show()
