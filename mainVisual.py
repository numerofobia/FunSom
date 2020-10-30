from music21 import *
from pylab import *
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import pygame
import music21 as mu21

win = tk.Tk()

win.title("FUNSOM")

win.resizable(False, False)

#definindo as funcoes
#FUNCAO SENO
def discrete_sin(theta, low_note, high_note):
    return int(high_note + int(high_note - low_note) * sin(theta))

def toca_sin():
    stream_seno = mu21.stream.Stream()
    pitchesList = [discrete_sin(n, 35, 60) for n in range(-12, 13)]
    [stream_seno.append(mu21.note.Note(midi=pitch, type = 'quarter')) for pitch in pitchesList]
    sp = mu21.midi.realtime.StreamPlayer(stream_seno)
    sp.play()
    stream_seno.show()

#funcao afim
def discrete_afim(parametro, low_note, high_note):
    return int((high_note-low_note) * 0.02 * parametro) + 55

def toca_afim():
    stream_afim = mu21.stream.Stream()
    pitchesList = [discrete_afim(n, 30, 82) for n in range(-5, 15)]
    [stream_afim.append(mu21.note.Note(midi=pitch, type = 'quarter')) for pitch in pitchesList]
    sp = mu21.midi.realtime.StreamPlayer(stream_afim)
    sp.play()
    stream_afim.show()

#funcao quadratica
def discrete_quad(parametro, low_note, high_note):
    return int(parametro ** 2) + 30

def toca_quad():
    stream_quad = mu21.stream.Stream()
    pitchesList = [discrete_quad(n, 30, 82) for n in range(-7, 8)]
    [stream_quad.append(mu21.note.Note(midi=pitch, type = 'quarter')) for pitch in pitchesList]
    sp = mu21.midi.realtime.StreamPlayer(stream_quad)
    sp.play()
    stream_quad.show()

#funcao exponencial
def discrete_exp(parametro, low_note, high_note):
    return int(0.08 * int(2 ** parametro)) + 30

def toca_exp():
    stream_exp = mu21.stream.Stream()
    pitchesList = [discrete_exp(n, 30, 82) for n in range(1, 11)]
    [stream_exp.append(mu21.note.Note(midi=pitch, type = 'quarter')) for pitch in pitchesList]
    sp = mu21.midi.realtime.StreamPlayer(stream_exp)
    sp.play()
    stream_exp.show()

ttk.Label(win, text = "FUNSOM").grid(column = 0, row = 0)

#Adicionando Botoes
action = ttk.Button(win, text = 'Função Afim', command = toca_afim)
action.grid(column = 0, row = 1)

action1 = ttk.Button(win, text = 'Função Quadrática', command = toca_quad)
action1.grid(column = 0, row = 2)

action2 = ttk.Button(win, text = 'Função Trigonométrica', command = toca_sin)
action2.grid(column = 0, row = 3)

action3 = ttk.Button(win, text = 'Função Exponencial', command = toca_exp)
action3.grid(column = 0, row = 4)

#stream.show()
win.mainloop()
