import wx
import wx.grid as gridlib
from wx import DefaultSize

class DisplayAreaView(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent=parent, size=DefaultSize)
    
    def CreateView(self):

        grid = gridlib.Grid(self)
        grid.CreateGrid(25,12)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(grid, 1, wx.EXPAND, border=1)
        self.SetSizer(vbox)
        
        return self
 
