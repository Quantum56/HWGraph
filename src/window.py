import tkinter as tk
from matplotlib import pyplot as plt
import os
import random

class MainWindow(tk.Frame):
    counter = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.button = tk.Button(self, text="Create new window", command=self.add_graph)
        self.button.pack(side="top")
        
        testlist = [random()*10,random()*10]

        i = 1
        while i < 5:
            testlist.append(random()*10)
            i += 1
        
        plt

    def add_graph(self):
        self.counter += 1
        t = tk.Toplevel(self)
        t.wm_title("Window #%s" % self.counter)
        l = tk.Label(t, text="This is window #%s" % self.counter)
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)
        


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('800x600')
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()