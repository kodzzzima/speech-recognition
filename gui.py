import wave
from tkinter import *
from tkinter import filedialog as fd

from recognition import recognition


def create_gui():
    def open_file():
        file_open = fd.askopenfilename(filetypes=[("WAV Files", "*.wav")])
        return wave.open(file_open)

    def insert_text():
        file = open_file()
        saved_text = recognition(file)
        text.insert(1.0, saved_text)
        file.close()

    root = Tk()

    text = Text(width=50, height=25)
    text.grid(columnspan=2)

    button = Button(text="Открыть", command=insert_text)
    button.grid(row=1, sticky=E)

    root.mainloop()
