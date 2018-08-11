import gettext


localdir = '../locale'
class LangSettings():
    def __init__(self):
        self.defaultValue = "zh_CN"
        global _
        l = gettext.translation('lang', localdir, languages=[self.defaultValue])
        _ = l.gettext
        
    def set_value(self, value):
        if value is None:
            l = gettext.translation('lang', localdir, languages=[self.defaultValue])
            _ = l.gettext
        else:
            l = gettext.translation('lang', localdir, languages=[value])
            _ = l.gettext
            
    def get_value(self):
        try:
            return _.gettext.GetLanguage()
        except:
            return self.defaultValue
    def get_lang(self):
        return _