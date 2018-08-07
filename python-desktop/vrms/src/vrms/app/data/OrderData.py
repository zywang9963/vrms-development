

class OrderData(object):

    def __init__(self, isDummyData):
        self.isDummyData = isDummyData
        if isDummyData:
            print("dummy data loaded")
        
    def getDummyData(self):
        self.dummyData = {"id":"0001", "orderNumber":"200000000001", "customerid":"10001", "orderDate":"2018-08-03 15:30:56", "creator":"20001"}
        return self.dummyData
