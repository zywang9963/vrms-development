'''
Created on 2018年8月4日

@author: Steven
'''
from wx.lib.agw.aui.tabart import ChromeTabArt
import wx

class TabPageView(ChromeTabArt):

    def __init__(self, parent, panel):
        ChromeTabArt.__init__(self)
        self.DrawTab(wx.DC, parent, panel, in_rect = wx.Rect2D, close_button_state = 1, paint_control=True)
        