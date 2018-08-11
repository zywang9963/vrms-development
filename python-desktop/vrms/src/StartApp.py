import wx

from vrms.views.main.GuiManager import GuiManager


class App(wx.App):
    def OnInit(self):
        self.manager = GuiManager(self.UpdateUI)
        self.frame = self.manager.GetFrame(1, None)
        self.frame.Show(True)
        return True

    def UpdateUI(self, type):
        self.frame.Show(False)
        self.frame = self.manager.GetFrame(type, None)
        self.frame.Show(True)


if __name__ == '__main__':
    app = App()
    app.MainLoop()
