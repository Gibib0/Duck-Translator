import tkinter as tk
from tkinter import messagebox
import random
import pygame
from pygame import mixer
import threading
import time
from PIL import Image, ImageTk

class DuckTranslator:
	def __init__ (self, root):
		self.root = root
		self.root.title('Duck Translator')
		self.root.geometry('600x500')

		# Music

		mixer.init()
		
		mixer.music.load('assets/sounds/background_sound.mp3')
		self.duck_sound = mixer.Sound('assets/sounds/duck_sound.mp3')
		self.holy_sound = mixer.Sound('assets/sounds/holy_sound.mp3')
		self.screamer_sound = mixer.Sound('assets/sounds/screamer_sound.mp3')
		self.ILoveU_sound = mixer.Sound('assets/sounds/ILoveU_sound.mp3')

		# Images

		background_image = Image.open('assets/images/background.jpg')
		self.background_photo = ImageTk.PhotoImage(background_image)

		self.duck_god = Image.open('assets/images/duck_god.jpeg')
		self.duck_god = self.duck_god.resize((200, 200), Image.Resampling.LANCZOS)
		self.duck_god_photo = ImageTk.PhotoImage(self.duck_god)

		self.rating_up = Image.open('assets/images/rating_up.jpeg')
		self.rating_up = self.rating_up.resize((200, 200), Image.Resampling.LANCZOS)
		self.rating_up_photo = ImageTk.PhotoImage(self.rating_up)

		self.screamer_image = Image.open('assets/images/screamer.jpeg')
		self.screamer_image = self.screamer_image.resize((200, 200), Image.Resampling.LANCZOS)
		self.screamer_photo = ImageTk.PhotoImage(self.screamer_image)

		self.romantic_image = Image.open('assets/images/romantic.jpg')
		self.romantic_image = self.romantic_image.resize((200, 200), Image.Resampling.LANCZOS)
		self.romantic_photo = ImageTk.PhotoImage(self.romantic_image)


		self.background_label = tk.Label(root, image=self.background_photo)
		self.background_label.place(relwidth=1, relheight=1)

		# DuckCounter

		self.duck_count = 0
		self.counter_running = True
		self.scarer_shown = False

		# InteractiveElements

		self.create_widgets()
		self.play_music()
		self.start_counter()
