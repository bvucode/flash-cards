from tkinter import *
import random

wordslist = []

with open("words-eng-ru.txt", "r") as file:
    for row in file:
        if not row:
            continue
        else:
            wordslist.append(row.replace("\n", ""))

class B(Button):
    def __init__(self, parent = None, **config):
        Button.__init__(self, parent, **config)
        self.startstop = 0
        self.config(command = self.changebutton)
        self.place(x = 160, y = 140)

    def startshowcards(self):
        self.lbl = Label(text = " ", fg = "yellow", bg = "black")
        self.lbl.place(x = 90, y = 60)
        while self.startstop == 1:
            try:
                word = random.choice(wordslist)
                self.lbl.configure(text = str(word))
                self.after(5000)
                self.update()
            except TclError:
                sys.exit()

    def changebutton(self):
        if self.startstop == 0:
            self.startstop = 1
            self.config(text = "pause")
            self.startshowcards()
        else:
            self.startstop = 0
            self.config(text = "show")
            self.startshowcards()

def main():
    root = Tk()
    B(text = "show")
    root.title("Flash Cards")
    root.geometry("400x175")
    root.configure(bg = "black")
    root.mainloop()

if __name__ == "__main__":
    main()
