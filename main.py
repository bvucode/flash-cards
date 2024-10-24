from tkinter import *
import random

wordslist = []

with open("./data/words.txt", "r") as file:
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
        self.place(x = 245, y = 150)

    def startshowcards(self):
        self.lbl = Label(text = " ", fg = "yellow", bg = "black")
        self.lbl.place(x = 140, y = 60)
        while self.startstop == 1:
            try:
                word = random.choice(wordslist)
                self.lbl.configure(text = str(word.replace(":", "  ")))
                self.after(5000)
                self.update()
            except TclError:
                break

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
    root.geometry("600x300")
    root.configure(bg = "gray")
    root.mainloop()

if __name__ == "__main__":
    main()
