import wx
import wx.grid as gridlib

class TreeView(wx.Panel):
    def __init__(self,parent, data):
        self.parent = parent
        wx.Panel.__init__(self, parent=parent)
        self.tree = wx.TreeCtrl(self)
        self.grid = gridlib.Grid(self)
        self.grid.CreateGrid(25,12)
        self.caption = "Tree View"
        
        self.data = [  'q',
                    ['a', ['2-1', '2-2', ['2-3', ['2-3-1', '2-3-2']]]],
                    ['z', ['3-1', '3-2']],
                    ['w', ['4-1', '4-2', '4-3']],
                    's'
                 ]
        print ("_init_ invoked")
        self.CreateView(data)
    
    def CreateView(self, data):
        self.FeedTreeData(data)
        selfSizer = wx.BoxSizer(wx.HORIZONTAL)
        selfSizer.Add(self.tree, 1, wx.EXPAND,border=1)
        selfSizer.Add(self.grid, 3, wx.EXPAND,border=1)
        self.SetSizer(selfSizer, deleteOld=True)
        
        
    def FeedTreeData(self,data):
        parent = self.tree.AddRoot("test")
        self.AddTreeNodes(parent,data)
        self.tree.Expand(parent)
        self.tree.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.OnItemExpanded, self.tree)
        self.tree.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.OnItemCollpased, self.tree)
        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self.tree)
        
    
    def AddTreeNodes(self, root, values):
        for node in values:
            if type(node) == str:
                self.tree.AppendItem(root,node)
            else:
                item = self.tree.AppendItem(root, node[0])
                self.AddTreeNodes(item, node[1])

    def OnItemExpanded(self,event):
        print ("OnItemExpanded: "+self.tree.GetItemText(event.GetItem()))

    def OnItemCollpased(self, event):
        print ("OnItemCollpased: "+self.tree.GetItemText(event.GetItem()))

    def OnSelChanged(self, event):
        print ("OnSelfChenged: "+self.tree.GetItemText(event.GetItem()))
        
