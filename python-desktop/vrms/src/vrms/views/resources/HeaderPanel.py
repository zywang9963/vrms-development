import wx
from vrms.views.resources.TreeView import TreeView
from vrms.views.oms.OrderListView import OrderList
from vrms.views.oms.CreateOrderView import CreateOrderView
import wx.lib.agw.flatnotebook as fnb
from wx.lib.agw.aui.auibook import AuiNotebook
from vrms.views.resources.test.TestView import TestView


class HeaderPanel(wx.Panel):
    def __init__(self, parent, menuItems, bodyPanel):
        wx.Panel.__init__(self, parent )
        
        self.SetBackgroundColour("#FFB90F")
        self.bodyPanel = bodyPanel
        
        #self.anb = AuiNotebook(bodyPanel)
        self.anb = fnb.FlatNotebook(bodyPanel,-1)

        nhbox = wx.BoxSizer(wx.HORIZONTAL)
        nhbox.Add(self.anb,-1,flag=wx.EXPAND, border=0)
        nvbox = wx.BoxSizer(wx.VERTICAL)
        nvbox.Add(nhbox,-1, flag=wx.EXPAND)
        self.bodyPanel.SetSizer(nvbox)
        self.bodyPanel.Layout()

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        for menuitem in menuItems:
            if  menuitem.get("visibility").strip().lower() == "true":
                btn = wx.Button(self,id = int(menuitem.get("key")), label =menuitem.get("des"), size=(100,80))
                btn.Bind(wx.EVT_BUTTON, self.menuHandler)
                hbox.Add(btn, flag=wx.LEFT|wx.BOTTOM|wx.ALIGN_CENTER_VERTICAL, border=0)
                hbox.Add((-1,10))
        vbox.Add(hbox,1, flag=wx.ALIGN_LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, border=1)
        self.SetAutoLayout(1)
        self.SetSizer(vbox)
        self.Layout()
        pass
    
    def menuHandler(self, event):
        id = event.GetId()
        if id == 9991:
            data = [  'a',
                        ['b', ['2-1', '2-2', ['2-3', ['2-3-1', '2-3-2']]]],
                        ['c', ['3-1', '3-2']],
                        ['d', ['4-1', '4-2', '4-3']],
                        'e'
                     ]
         
            treeview = TreeView(self.bodyPanel,data)
            self.anb.AddPage(treeview, treeview.caption, select=True)
            vbox = wx.BoxSizer(wx.VERTICAL)
            vbox.Add(self.anb,-1, flag=wx.EXPAND|wx.ALL, border=1)
            self.bodyPanel.SetSizer(vbox)
            self.bodyPanel.Layout()
        elif id ==1002:
            orderlist = OrderList(self.bodyPanel)
            self.anb.AddPage(orderlist, orderlist.caption , select=True)
            vbox = wx.BoxSizer(wx.VERTICAL)
            vbox.Add(self.anb,-1, flag=wx.EXPAND|wx.ALL, border=1)
            self.bodyPanel.SetSizer(vbox)
            self.bodyPanel.Layout()
        elif id == 1001:
            createorder = CreateOrderView(self.bodyPanel)
            self.anb.AddPage(createorder, createorder.caption,  select=True)
            vbox = wx.BoxSizer(wx.VERTICAL)
            vbox.Add(self.anb,-1, flag=wx.EXPAND|wx.ALL, border=1)
            self.bodyPanel.SetSizer(vbox)
            self.bodyPanel.Layout()
        elif id == 9992:
            testView = TestView(self)
            self.anb.AddPage(testView, testView.caption,  select=True)
            vbox = wx.BoxSizer(wx.VERTICAL)
            vbox.Add(self.anb,-1, flag=wx.EXPAND|wx.ALL, border=1)
            self.bodyPanel.SetSizer(vbox)
            self.bodyPanel.Layout()