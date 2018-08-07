from wx.lib.agw.aui.auibook import AuiNotebook
import wx

class MyAuiNotebook(AuiNotebook):

    def __init__(self, parent, panel):
        AuiNotebook.__init__(self, parent=parent)
        anb = AuiNotebook(parent, -1, size=(800,600))
        anb.AddPage(panel, panel.caption, select = True,  tooltip="test tab")
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(anb,1, flag=wx.EXPAND, border=2)
        parent.SetSizer(hbox, deleteOld=True)
        parent.SetAutoLayout(1)
        parent.Layout()
        
        #vbox = wx.BoxSizer(wx.VERTICAL)
        #vbox.Add(self,  flag=wx.EXPAND|wx.ALL, border=2)
        #parent.SetSizer(vbox)

        
 
        