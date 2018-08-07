import wx

class CreateOrderView(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.parent = parent
        self.caption = "Create Order"
        self.control = wx.Control
        self.bitmap = wx.Bitmap
        self.active = True
        self.SetAutoLayout(1)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        tx = wx.StaticText(self,label="test page")
        hbox.Add(tx,1, flag=wx.LEFT|wx.BOTTOM|wx.EXPAND, border=5)
        vbox.Add(hbox,1, flag=wx.LEFT|wx.BOTTOM|wx.EXPAND, border=5)
        
        selfsizer = wx.BoxSizer(wx.VERTICAL)
        selfsizer.Add(vbox, 1, flag=wx.EXPAND)
        self.SetSizer(selfsizer)
        self.Layout()
        



        
        
      