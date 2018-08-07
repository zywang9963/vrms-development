from vrms.views.main.MainWindow import MainFrame

class GuiManager():
    def __init__(self, UpdateUI):
        self.UpdateUI = UpdateUI
        self.frameDict = {} # 用来装载已经创建的Frame对象

    def GetFrame(self, type):
        frame = self.frameDict.get(type)

        if frame is None:
            frame = self.CreateFrame(type)
            self.frameDict[type] = frame
        return frame

    def CreateFrame(self, type):
        if type == 0:
            #return LoginFrame(parent=None, id=type, UpdateUI=self.UpdateUI)
            return
        elif type == 2:
            return MainFrame(parent=None, id=type, UpdateUI=self.UpdateUI)