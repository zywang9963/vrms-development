import wx
import wx.lib.agw.aui as aui

class MyAuiMgr(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self,parent=parent)
        self.SetAutoLayout(1)

        
    def addPanel(self,child):
        mgr = aui.AuiManager()
        mgr.SetManagedWindow(self)
        mgr.AddPane1(child, aui.AuiPaneInfo().Left().Caption(child.caption))
        mgr.Update()
        mgr.Bind(wx.EVT_CLOSE, self.OnClose)
        print(mgr.GetAllPanes())
        self.Layout()
    
    def OnClose(self, event):
        self.mgr.UnInit()
        event.Skip()
        