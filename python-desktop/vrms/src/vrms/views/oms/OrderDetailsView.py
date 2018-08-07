import wx
from vrms.app.data.OrderData import OrderData

class OrderDetail(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.parent = parent
        self.dummyData = self.getDummyData()
        
    def getDummyData(self):
        data = OrderData(dummy=True)
        return data