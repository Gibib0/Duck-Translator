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
		mixer.music.set_volume(0.3)

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
		self.counter_running = False
		self.scarer_shown = False

		# InteractiveElements

		self.create_widgets()

		self.show_welcome_message()
		
		self.play_music()
		self.duck_counter()


	def show_welcome_message(self):
		messagebox.showwarning('From this moment, ducks will come to you every second. (Don`t wait until 300...)\n Press OK to start.')

	def create_widgets(self):
		label = tk.Label(self.root, text = 'DUCK Translator',
										font=('Comic Sans', 20, 'bold'), bg='white', relief='raised')
		label.pack(pady=10)

		self.text_input = tk.Entry(self.root, width=50, height=4, bg='pink', font=('Comic Sans', 12))
		self.text_input.pack(pady=5)
		self.text_input.insert(0, 'Enter your text here.....')
		self.text_input.bind('<FocusIn>', self.clear_placeholder)

		translate_btn = tk.Button(self.root, text='Translate to Duck',
															command=self.translate_text, bg='yellow', 
															font=('Comic Sans', 10))
		translate_btn.pack(pady=10)

		self.text_output = tk.Text(self.root, width=50, height=4, bg='pink', font=('Comic Sans', 10))
		self.text_output.pack(pady=10)

		praise_btn = tk.Button(self.root, text='Praise the Duck',
													command=self.praise_duck, bg='green', fg='white',
													font=('Comic Sans', 12, 'bold'))
		praise_btn.pack(pady=10)

		self.counter_label = tk.Label(self.root, text='Ducks arrived: 0 🦆',
																font=('Comic Sans', 12), bg='lightgrey')
		self.counter_label.pack(side=tk.BOTTOM, pady=10)


	def clear_placeholder(self, event):
		if self.text_input.get() == "Enter your text here.....":
			self.text_input.delete(0, tk.END)

	def play_music(self):
		mixer.music.play(-1)

	def pause_music(self):
		mixer.music.pause()

	def resume_music(self):
		mixer.music.unpause()

	def duck_counter(self):
		self.counter_running = True
		def counter_thread():
			while self.counter_running:
				time.sleep(1)
				self.duck_count += 1
				self.root.after(0, self.update_counter_label)
		
		thread = threading.Thread(target=counter_thread, daemon=True)
		thread.start()

	def update_counter_label(self):
		self.counter_label.config(text=f'{self.duck_count} 🦆')

		if self.duck_count == 300 and not self.scarer_shown:
			self.screamer = True
			self.screamer()

	def screamer(self):
		self.pause_music()

		screamer_window = tk.Toplevel(self.root)
		screamer_window.geometry('400x400')
		screamer_window.attributes('-topmost', True)

		label = tk.Label(screamer_window, image = self.screamer_photo)
		label.pack()

		self.screamer_sound.play()

		self.root.after(1000, lambda: self.close_screamer(screamer_window))

	def close_screamer(self, window):
		window.destroy()
		self.resume_music()

	def translate_text(self):
		self.duck_sound()
		user_text = self.text_input.get()

		if 'Я тебя люблю' in user_text.lower():
			self.show_love()
			return
		
		duck_syllables = ['Quack', 'quack-quack', 'quack', 'HONK', 'honk-honk', 'Quacky', 'quacky', 'Quack?!', '~quack~', '...quack', '(webble)', '(splach)', '(paddle)', 'Quack~ quackle~']

		duck_words = [random.choice(duck_syllables) for _ in range(random.randint(3, 10))]
		duck_translation = ' '.join(duck_words)

		self.text_output.delete(1.0, tk.END)
		self.text_output.insert(tk.END, duck_translation)

	def show_love(self):
		self.pause_music()
		self.ILoveU_sound.play()

		love_window = tk.Toplevel(self.root)
		love_window.geometry('300x500')

		label = tk.Label(love_window, image=self.romantic_photo)
		label.pack(pady=10)

		close_btn = tk.Button(love_window, text='OK', command=lambda: self.close_love_window(love_window), bg = 'pink', font=('Comic Sans', 12))
		close_btn.pack(pady=10)

	def close_love_window(self, window):
		window.destroy()
		messagebox.showinfo('And I love u /ᐠ｡ꞈ｡ᐟ\ ')
		self.resume_music()

	def praise_duck(self):
		self.pause_music()
		self.holy_sound.play()

		praise_window = tk.Toplevel(self.root)
		praise_window.geometry('300x300')

		label = tk.Label(praise_window, image=self.rating_up_photo)
		label.pack(pady=20)

		text_label = tk(praise_window, text='U made the right choice!\n The Great Duck accepred ur praise.', font=('Comic Sans', 10))
		close_btn = tk.Label(praise_window, text='OK', command=lambda: self.slode_praise_window(praise_window), bg='skyblue', font=('Comic Sans', 12))
		close_btn.pack(pady=10)

		next_btn = tk.Button(praise_window, text='OK', command=lambda: self.show_holy_duck(praise_window), bg='lightgreen', font=('Comic Sans', 12))
		next_btn.pack(pady=10)

	def show_holy_duck(self, first_window):
		first_window.destroy()

		holy_window = tk.Toplevel(self.root)
		holy_window.geometry('350x400')

		label = tk.Label(holy_window, image=self.duck_god_photo)
		label.pack(pady=20)

		text_label = tk.Label(holy_window, text='Blessed are those who praise the Duck~!', font=('Comic Sans', 12, 'bold'))
		text_label.pack(pady=10)

		close_btn = tk.Button(holy_window, text='Amen', command=lambda: self.close_holy_window(holy_window), bg='gold', font=('Comic Sans', 12))

		close_btn.pack(pady=10)

		self.holy_sound.play()

	def close_holy_window(self, window):
		window.destroy()
		self.resume_music()

		def on_closing(self):
			self.counter_running = False
			self.root.destroy()

if __name__ == '__main__':
	root = tk.Tk()
	app = DuckTranslator(root)
	root.protocol('WM_DELETE_WINDOW', app.on_closing)
	root.mainloop()
