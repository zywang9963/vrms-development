class OrderItemData(object):
    def __init__(self, isDummyData):
        self.isDummyData = isDummyData
        
    def getDummyData(self):
        self.dummyData = {"id":"1001","orderItemId":"200000000001","partId":"0000001","qty":"2","price":"999.99"}
        return self.dummyData