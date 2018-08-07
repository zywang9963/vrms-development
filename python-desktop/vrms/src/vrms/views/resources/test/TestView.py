import wx
import wx.lib.agw.aui as aui

class TestView(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.caption = "Test View Page"
        self.tx = wx.StaticText(self, id=1, label="test label:")
        self.tl = wx.TextCtrl(self, id=2, value="this is my test")
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.tx,1, flag=wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL,border=5)
        hbox.Add(self.tl,1, flag=wx.EXPAND|wx.ALIGN_LEFT|wx.ALIGN_CENTER_VERTICAL|wx.ALL,border=5)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox)
        
        btn = wx.Button(self, id=3, label="show tabpage")
        btn.Bind(wx.EVT_BUTTON, self.actionHandler)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(btn, 1, flag=wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,border=5)
        vbox.Add(hbox1)
        self.SetSizer(vbox, deleteOld=True)
        self.SetAutoLayout(1)
        self.Layout()
        
    def actionHandler(self,event):
        id = event.GetId()
        if id == 3:
            self.dg = wx.Dialog(self, wx.Center, title="dialog test")
            self.tx = wx.StaticText(self.dg, label="test dialog")
            self.btn = wx.Button(self.dg, id=10, label="transfer data")
            self.btn.Bind(wx.EVT_BUTTON, self.OnBtnClick)
            hbox = wx.BoxSizer(wx.HORIZONTAL)
            hbox.Add(self.tx,-1, flag=wx.ALIGN_CENTER, border=5)
            hbox.Add(self.btn,-1, flag=wx.ALIGN_CENTER, border=5)
            vbox = wx.BoxSizer(wx.VERTICAL)
            vbox.Add(hbox,-1, flag=wx.ALIGN_LEFT|wx.EXPAND, border=5)
            self.dg.SetSizer(vbox, deleteOld=True)
            self.dg.Layout()
            self.dg.ShowModal()
            
    def OnBtnClick(self, event):
        id = event.GetId()
        self.tl.SetValue("Data update successfully")
        self.dg.Destroy()
        event.Skip()
        
        
        