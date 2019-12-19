import tkinter as tk
from matplotlib import pyplot as plt
import os
from random import random
from PIL import ImageTk, Image
from test import graph_create

class MainWindow(tk.Frame):
    counter = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.button1 = tk.Button(self, text="Graph Subplot", command=self.add_graph)
        self.button1.pack(side="bottom")
        
        testlist = [random()*10,random()*10]

        i = 1
        while i < 5:
            testlist.append(random()*10)
            i += 1
        

    def add_graph(self):
        graph_create([1, 2], 'f2')
        self.counter += 1
        t = tk.Toplevel(self)
        t.wm_title("Graph #%s" % self.counter)
        l1 = tk.Label(t, text="Graph #%s" % self.counter)
        l1.pack(side="top", fill="both", expand=True, padx=100, pady=100)
        print(os.getcwd())
        img = ImageTk.PhotoImage(Image.open("foo.png"))
        l2 = tk.Label(t, image=img)
        l2.pack(side="bottom", fill="both", expand=True)

        # dir_path = os.path.dirname(os.path.realpath(__file__))
        # print(dir_path)
        


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('800x600')
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()