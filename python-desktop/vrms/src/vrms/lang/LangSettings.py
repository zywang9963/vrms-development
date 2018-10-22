import gettext
from vrms.app.sys.DBUtilities import DBUtilities
from vrms.app.sys.SysUtilies import SysUtilies

localdir = '../locale'
class LangSettings():
    def __init__(self):
        self.defaultValue = self.get_defaultLang()
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
    
    def get_defaultLang(self):
        conn = DBUtilities().getConn()
        c = conn.cursor()
        cursor = c.execute("SELECT ID,LANG_ID,LANG_DES_ENG,LANG_DES_CN FROM LOCALE_SETTINGS ")
        print(cursor.fetchall())
        num = 0
        for cur in cursor:
            num+=1
            print("num :" + cur[0])
            #return cur[1]
        conn.close()
        return "zh_CN"
        