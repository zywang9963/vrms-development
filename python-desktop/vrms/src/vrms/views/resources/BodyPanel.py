import wx

class BodyPanel(wx.Panel):
    def __int__(self, parent):
        wx.Panel.__init__(self, parent )
        
        self.SetBackgroundColour("#EBEBEB")
        self.SetAutoLayout(1)
        self.Layout()