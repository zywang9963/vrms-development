import wx
from xml.etree import ElementTree as ET

xmlPath = '../resource/xml/menu/menus.xml'


class SystemMenus(wx.MenuBar):

    def __init__(self, parent):
        wx.MenuBar.__init__(self)
        self.parent = parent
        self.loadMenus()
       
    def loadMenus(self):
        elementTree = ET.parse(xmlPath)
        allnodes = elementTree.iter(tag="menu")
        if allnodes is not None:
            self.buildMenu(self, allnodes, None)
            self.parent.SetMenuBar(self)
            self.Bind(wx.EVT_MENU, self.menuHandler)
        
    def buildMenu(self, menubar, allnodes, parentMenu):
        for child in allnodes:
            if child.tag == "menu":
                menu = wx.Menu()
                if child.get("parent") == "sysmenu":
                    menubar.Append(menu, title=child.get("des"))
                if parentMenu is not None:
                    parentMenu.Append(wx.ID_ANY, child.get("des"), menu)
                    
                self.buildMenu(menubar, child, menu)
            elif child.tag == "menuitem":
                # parentMenu.AppendSeparator()
                menuitem = wx.MenuItem(parentMenu, id=int(child.get("key")), text=child.get("des"), kind=wx.ITEM_NORMAL)
                parentMenu.Append(menuitem)
            elif child.tag == "seperator":
                parentMenu.AppendSeparator()

    def menuHandler(self, event):
        id = event.GetId()
        if id == 101:
            pass
        elif id == 102:
            pass
        elif id == 201:
            pass
        elif id == 202:
            pass
        elif id == 204:
            dl = wx.Dialog(self, wx.Center, title="vrms - 提示信息", size=(310,200))
            tx = wx.StaticText(dl, label="The initiallization process will erase all business data from your system, and reset all settings to default! \n Do you want to continue?")
            tx.Wrap(280)
            btn_confirm = wx.Button(dl, id=1, label="Confirm", size=(80,30))
            btn_cancel = wx.Button(dl, id=1, label="Cancel", size=(80,30))
            
            hboxtx = wx.BoxSizer(wx.HORIZONTAL)
            hboxtx.Add(tx,1, flag=wx.ALIGN_CENTER|wx.TE_BESTWRAP, border= 10)
            
            hboxbtn = wx.BoxSizer(wx.HORIZONTAL)
            hboxbtn.Add(btn_confirm,1, flag=wx.ALIGN_LEFT, border=5)
            hboxbtn.Add(btn_cancel,1, flag=wx.ALIGN_LEFT, border=5)
            
            vbox = wx.BoxSizer(wx.VERTICAL)
            vbox.Add((-1,30))
            vbox.Add(hboxtx,1, flag=wx.ALIGN_CENTRE_HORIZONTAL|wx.ALIGN_TOP, border=5)
            vbox.Add((-1,20))
            vbox.Add(hboxbtn,1, flag=wx.ALIGN_CENTRE_HORIZONTAL|wx.ALIGN_BOTTOM, border=5)
            dl.SetSizer(vbox)
            dl.Layout()
            dl.ShowModal()
           
            
            
            
            
