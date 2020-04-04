import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from matplotlib import style
import matplotlib.animation as animation
style.use('ggplot')

fig = Figure(figsize=(7, 5))
ax = fig.add_subplot(111)

def animate(i):
    pullData = open('sampleData.txt','r').read()
    dataList = pullData.split("\n")
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))

    ax.clear()
    ax.plot(xList,yList)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.UIinit()

    def UIinit(self):
        self.geometry("640x550+250+50")
        self.configure(background='#95A5A6')
        self.title("Crypto visualizer")
        
        #THE HEADING FRAME WITH LABEL WIDGET PACKED IN IT..
        self.frame = tk.Frame(bg="#17202A",bd=2)
        self.heading = tk.Label(self.frame,text="Welcome to Crypto Visualizer",font="Lucida 26",fg='white',bg="#17202A")
        self.heading.pack(side=tk.TOP,fill=tk.BOTH)
        self.grid_columnconfigure(0,weight=1)
        self.frame.grid(row=0,sticky='nsew')

        # ADDING THE MATPLOTLIB GRAPH
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.get_tk_widget().grid(sticky='nsew')

        #PLOTTING THE DATA
        ax.set_title ("Scatter Plot)", fontsize=16)
        ax.set_ylabel("Y", fontsize=14)
        ax.set_xlabel("X", fontsize=14)

        self.canvas.draw()


if __name__ == "__main__":
    root = App()
    ani = animation.FuncAnimation(fig,animate,interval=1000)
    root.mainloop()