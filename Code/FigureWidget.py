import sys, numpy as np, time, math
from typing_extensions import Self

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout,QHBoxLayout, QGridLayout, QPushButton, QLineEdit,QMessageBox
from PyQt6.QtGui import QIntValidator

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
# ------------------------------------------------------------------
# ---- class FigureWidget
# ------------------------------------------------------------------
class FigureWidget(FigureCanvas):
    """ Matplotlib Figure Widget  """
    # static attribute
    colors = np.array(["red","green","blue","yellow","pink","orange","purple","beige","brown","gray","cyan","magenta", "black"])

    def __init__(self : Self, width : int =10, height : int=5, dpi : int=100) -> None:
        # create Figure
        #self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)    # explicite call of super constructor
        FigureCanvas.updateGeometry(self)
        self.setMinimumSize(800, 400)

    def scatter(self : Self,x : list[float],y : list[float], current : int|None = None, clear : bool =True , color : int|None = None) -> None:
        colorCurrent = len(FigureWidget.colors) -1
        colorSelection = 0 if not isinstance(color, int) else color 
        
        if clear : self.axes.clear()

        if len(x)> 1 :
            self.axes.scatter(x,y,25, c=FigureWidget.colors[colorSelection])
        # self.axes.plot() | axes c'est la figure de matplotlib
        if isinstance(current, int):
            self.axes.scatter(x[current],y[current],100, c=FigureWidget.colors[colorCurrent])

        #self.axes.annotate(str(i),(xs[i]+10,ys[i]))
        self.axes.axis('on')

        try:
            self.fig.canvas.draw()
        except Exception:
            time.sleep(0.5)
            self.fig.canvas.draw()
    # TODO : Def plot()
    