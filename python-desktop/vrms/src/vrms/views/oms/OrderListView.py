import wx
import wx.grid as gridlib
from  wx.lib.rcsizer import RowColSizer

CONFIRM=wx.NewId()
CANCEL=wx.NewId()
class OrderList(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.parent = parent
        self.control = wx.Control
        self.caption = "Order List"
        self.bitmap = wx.Bitmap
        self.active = True
        self.SetAutoLayout(1)
        self._initUI_()
        self.id = "1001"
        
    def _initUI_(self):
        #panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        orderidlabel = wx.StaticText(self, label="Order Number")
        hbox1.Add(orderidlabel, flag=wx.LEFT, border=8)
        orderidinput = wx.TextCtrl(self)
        hbox1.Add(orderidinput, 1)
        vbox.Add(hbox1, flag=wx.LEFT|wx.RIGHT|wx.TOP,border=10)
        
        vbox.Add((-1, 25))
        
        btnConfirm = wx.Button(self, label = 'Confirm', size=(70,30))
        btnCancel = wx.Button(self, label ='Cancel', size=(70,30))
        btnsizer = wx.BoxSizer(wx.HORIZONTAL)
        btnsizer.Add(btnConfirm)
        btnsizer.Add(btnCancel, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(btnsizer,flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)
        
        vbox.Add((-1, 25))
        
        grid = gridlib.Grid(self)
        grid.CreateGrid(10, 20)
        gsizer = wx.BoxSizer(wx.HORIZONTAL)
        gsizer.Add(grid, flag=wx.EXPAND|wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(gsizer, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=10)
        
        self.SetSizer(vbox)
        self.SetAutoLayout(1)
        self.Layout()
        

    

     
