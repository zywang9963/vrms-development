
import wx
from vrms.views.resources.HeaderPanel import HeaderPanel
from vrms.views.resources.BodyPanel import BodyPanel

class WorkBenchPanel(wx.Panel):
    def __init__(self, parent, menuItems):
        wx.Panel.__init__(self, parent)
        
        
        bodyPanel = BodyPanel(self)
        headerPanel = HeaderPanel(self,menuItems,bodyPanel)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(headerPanel,1, flag=wx.EXPAND|wx.ALL, border=0)
        vbox.Add(bodyPanel,99, flag=wx.EXPAND|wx.ALL, border=0)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(vbox,-1, flag=wx.EXPAND)
        self.SetSizer(hbox)
        self.SetAutoLayout(1)
        self.Layout()      
