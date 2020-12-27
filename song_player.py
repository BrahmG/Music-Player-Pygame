# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 15:36:31 2020

@author: bpash
"""

import pygame
import tkinter as tk
from tkinter.filedialog import askdirectory
import os
import winsound

font='Helvetica 12 bold'

music_player=tk.Tk()
music_player.title('Music in Life')
music_player.geometry('450x350')



directory=askdirectory()
os.chdir(directory)
song_list=os.listdir()
print(os.getcwd())



play_list=tk.Listbox(music_player,font=font,
					 bg='yellow',selectmode=tk.SINGLE)

for i in song_list:
	pos=0
	play_list.insert(pos,i)
	pos+=1
	
	
pygame.init()
pygame.mixer.init()

#control functions

def play():
	pygame.mixer.music.load(play_list.get(tk.ACTIVE))
	var.set(play_list.get(tk.ACTIVE))
	pygame.mixer.music.play()



def stop():
	pygame.mixer.music.stop()
	


def pause():
	pygame.mixer.music.pause()


def unpause():	
	pygame.mixer.music.unpause()
	
def VolAdj(val):

    pygame.mixer.music.set_volume(val)
	
#creating buttons

Button1=tk.Button(music_player,width=5,height=3,font=font,
				  text='║║',command=play,bg='GREEN', fg='white')

Button2=tk.Button(music_player,width=5,height=3,font=font,
				  text='STOP',command=stop,bg='RED', fg='white')

Button3=tk.Button(music_player,width=5,height=3,font=font,
				  text='PAUSE',command=pause,bg='PURPLE', fg='white')

Button4=tk.Button(music_player,width=5,height=3,font=font,
				  text='║║',command=unpause,bg='BLUE', fg='white')

#VolSlider=tk.Scale(music_player,length=140,label=' Volume ',orient = 'horizontal', fg = 'black', bg='light blue', command = VolAdj)
	
	
	
var=tk.StringVar()
song_title=tk.Label(music_player,font=font, textvariable=var)

#pack method to arrnge buttons horizontally
song_title.pack()
Button1.pack(fill='x')
Button2.pack(fill='x')
Button3.pack(fill='x')
Button4.pack(fill='x')
play_list.pack(fill='both',expand='yes')

music_player.mainloop()
	

