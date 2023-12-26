import tkinter as tk 
from tkinter import ttk
import pygame

# генерация ключа
def generate_key():
    input_block = inp_entry.get()
    if not input_block:
            return
    
    # 2 блок (сдвиг на 3 символа вправо)
    block2 = ''.join([chr((ord(char) - ord('A') + 3) % 26 + ord('A')) if char.isalpha() else chr((ord(char) - ord('0') + 3) % 26 + ord('0')) if char.isdigit() else char for char in input_block])

    # 3 блок (сдвиг на 5 символов влево)
    block3 = ''.join([chr((ord(char) - ord('A') - 5) % 26 + ord('A')) if char.isalpha() else chr((ord(char) - ord('0') - 5) % 26 + ord('0')) if char.isdigit() else char for char in input_block])

    generated_key = f"{input_block}-{block2}-{block3}"  

    gener_ex.config(state="normal")
    gener_ex.delete(0, tk.END)
    gener_ex.insert(0, generated_key)
    gener_ex.config(state="readonly")


# создание окна с изображением
window = tk.Tk()
window.geometry('550x400')
window.title('Generate  a   K E Y')
bg_img = tk.PhotoImage(file='may.png')

lbl_bg = tk.Label(window, image=bg_img)
lbl_bg.place( relwidth=1, relheight=1)


# поле для ввода первого блока ключа
frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='center')

lbl = tk.Label(frame, text='Введите 1 блок ключа', font=('Garamond', 15))
lbl.grid(column=0, row=0, padx=10)

inp_entry = tk.Entry(frame, width=15)
inp_entry.grid(column=0, row=1, padx=10, pady=10)

# поле для отображения сгенерированного ключа
gener_lbl = tk.Label(frame, text='Сгенерированный ключ:', font=('Garamond', 15))
gener_lbl.grid(column=0, row=3, padx=10, pady=10)

gener_ex = tk.Entry(frame, state='readonly', width=20)
gener_ex.grid(column=0, row=4, padx=10, pady=10)

# кнопка генерации ключа
gener_but = tk.Button(frame, text='Сгенерировать ключ', font=('Garamond', 15), command=generate_key)
gener_but.grid(column=0, row=2, padx=10, pady=10)


# загрузка и воспроизведение музыки
 
pygame.mixer.init()
pygame.mixer.music.load("ducks.mp3")
pygame.mixer.music.play(-1)


window.mainloop()





