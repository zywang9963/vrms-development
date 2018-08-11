import wx
from vrms.views.resources.NotebookView import NotebookView
from vrms.views.resources.SystemMenusView import SystemMenus
from vrms.lang.LangSettings import LangSettings

xmlPath ='../resource/xml/menu/menus.xml'


class MainFrame(wx.Frame):
    pass
    def __init__(self, parent=None ,id=-1, UpdateUI = None, lang = None):
        LangSettings().set_value(lang)
        _ = LangSettings().get_lang()
        self.frame = wx.Frame
        self.frame.__init__(self, parent, title=_("Vehicle Repair & Maintenance System"),  name="vrms",)
        self.Center()
        self.statusbar = self.CreateStatusBar(number=1, id=0)
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-3, -2, -1])
        
        self.statusbar.SetStatusText("",0)
        self.statusbar.SetStatusText("",1)
        self.statusbar.SetStatusText(_("Vehicle Repair & Maintenance System"),2)
        
        self.Maximize(maximize=True)
        SystemMenus(self)


        nb = NotebookView(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(nb,-1, flag=wx.EXPAND)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox,-1, flag=wx.EXPAND)
        self.SetSizer(vbox)
        self.SetAutoLayout(1)
        self.Layout()
        
    def _initUI_(self):
        self._refresh_()
        self.SetAutoLayout(1)
        panel = wx.Panel(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(panel, 1, wx.EXPAND)
        self.SetSizer(hbox)
        self.Layout()

    def _refresh_(self):
        print (self.Children)



