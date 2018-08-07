'''
Created on 2018年8月3日

@author: Steven
'''
import wx
from xml.etree import ElementTree as ET

from vrms.views.resources.WorkBenchView import WorkBenchPanel

xmlPath = '../resource/xml/menu/menusfortab.xml'


class NotebookView(wx.Notebook):
    def __init__(self, parent, ):
        wx.Notebook.__init__(self, parent=parent)
        self.parent = parent
        elementTree = ET.parse(xmlPath)
        allnodes = elementTree.iter(tag="menu")
        if allnodes is not None:
            self.buildMenu(allnodes)
        
        self.SetAutoLayout(1)
        self.Layout()
        
    def buildMenu(self, allnodes):
        for child in allnodes:
            if child.tag == "menu" and child.get("visibility").strip().lower() == "true":
                if child.get("parent") == "sysmenu":
                    self.AddPage(WorkBenchPanel(self,child), child.get("des"))
                else:
                    pass

