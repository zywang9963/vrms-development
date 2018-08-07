import wx
from wx import Cursor
from xml.dom.minidom import parse
from xml.etree import ElementTree as ET
from TreeView import TreeView
from DisplayAreaView import DisplayAreaView

xmlPath ='../../../../resource/xml/menu/menus.xml'
class MainFrame(wx.Frame):
    pass
    def __init__(self, parent=None ,id=-1, UpdateUI = None):
        self.frame = wx.Frame
        self.frame.__init__(self, parent, title="My test",  name="test")
        self.Center()
        self.setupMenuBar()
        self.treePanel = None
        #self.Maximize(True)
        self.UpdateUI = UpdateUI
        #self.SetBackgroundColour("#000011")
        #self.createUI()

    def setupMenuBar(self):
            self.CreateStatusBar()
            menubar = wx.MenuBar()
            elementTree = ET.parse(xmlPath)
            allnodes = elementTree.iter(tag="menu")
            #p=per.findall("menu")
            if allnodes is not None:
                self.buildMenu(menubar, allnodes, None)
            self.SetMenuBar(menubar)
            self.Bind(wx.EVT_MENU, self.menuHandler)
            
    def buildMenu(self, menubar, allnodes, parentMenu):
        for child in allnodes:
            print(child.get("des"))
            if child.tag == "menu":
                menu = wx.Menu()
                if child.get("parent") == "sysmenu":
                    menubar.Append(menu, title = child.get("des"))
                if parentMenu is not None:
                    parentMenu.Append(wx.ID_ANY,child.get("des"), menu )
                self.buildMenu(menubar, child, menu)
            elif child.tag == "menuitem":
                menuitem = wx.MenuItem(parentMenu,id = int(child.get("key")),text = child.get("des"),kind=wx.ITEM_NORMAL)
                parentMenu.Append(menuitem)
                parentMenu.AppendSeparator()
                 
    def menuHandler(self, event):
        id = event.GetId()
        if id == 1200:
            if self.treePanel is None:
                self.treePanel = TreeView(self).CreateView()
                self.displayAreaPanel = DisplayAreaView(self).CreateView()
                
                hbox = wx.BoxSizer(wx.HORIZONTAL)
                hbox.Add(self.treePanel, 1, wx.EXPAND)
                hbox.Add(self.displayAreaPanel, 3, wx.EXPAND)
                self.SetSizer(hbox)
                print("print new tree")
            else:
                self.treePanel.Show()
                print("show the existing tree")
        elif id == 1300:
            if self.treePanel.IsShown():
                self.treePanel.Destroy()
                self.treePanel = None
            if self.displayAreaPanel.IsShown():
                self.displayAreaPanel.Destroy()
                self.displayAreaPanel = None
            

        
    def createUI(self):
            panel = wx.Panel(self,-1)
            vbox = wx.BoxSizer(wx.VERTICAL)
            vbox.Add(panel, 1, wx.EXPAND)







