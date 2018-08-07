import wx


class TreeView(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent=parent, size=(200,600))
    
    def CreateView(self):
        
        self.tree = wx.TreeCtrl(self,size=(200,600))
        parent = self.tree.AddRoot("test")
        self.AddTreeNodes(parent, self.GetTreeData())
        self.tree.Expand(parent)
        self.tree.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.OnItemExpanded, self.tree)
        self.tree.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.OnItemCollpased, self.tree)
        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, self.tree)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.tree, 1, wx.EXPAND,border=1)
        self.SetSizer(vbox)

        return self
        
        
    def GetTreeData(self):
        data = [  '1',
                    ['2', ['2-1', '2-2', ['2-3', ['2-3-1', '2-3-2']]]],
                    ['3', ['3-1', '3-2']],
                    ['4', ['4-1', '4-2', '4-3']],
                    '5'
                 ]
        return data
        
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
        
