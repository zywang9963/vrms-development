import wx

from vrms.views.main.GuiManager import GuiManager
from vrms.lang.LangSettings import LangSettings
from vrms.app.sys.SysUtilies import SysUtilies
from vrms.app.sys.DBUtilities import DBUtilities

class App(wx.App):
    def OnInit(self):
        #SysUtilies().SystemInit(DBUtilities().getConn())
        self.manager = GuiManager(self.UpdateUI)
        print("the default language is :"+LangSettings().get_defaultLang())
        self.frame = self.manager.GetFrame(1, LangSettings().get_defaultLang())
        self.frame.Show(True)
        return True

    def UpdateUI(self, type):
        self.frame.Show(False)
        self.frame = self.manager.GetFrame(type, LangSettings.get_defaultLang())
        self.frame.Show(True)


if __name__ == '__main__':
    app = App()
    app.MainLoop()
