from sqlalchemy.orm.session import sessionmaker
from tools.DataBase.Connect import conection
from tools.EndPoints.HotelPro import HotelPro


class EndPointHandle:
    endpoints={2:HotelPro}
    def __init__(self, inputs):
        self.connODM = conection().conODM()
        self.connORM = conection().conORM()

        self.status = 200
        self.msg = "0"
        self.type = "text/plain"
        Session = sessionmaker(bind=self.connORM)
        self.session = Session()
        if inputs["company"] in self.endpoints:
            #This just will apply to systems registred on the endpoint handle
            targetCls=self.endpoints[inputs["company"]]()
            retVal=getattr(targetCls, "process")(inputs)
            self.msg= retVal["value"]
            self.type=retVal["type"]
            self.status=retVal["status"]


if __name__ == '__main__':
    d={'table': 304,
       'company': 2,
       'products': [{'order': 250, 'owner': {'code': '1', 'extra': 'null',
                                             'name': 'CodeService, SRL', 'document': '131353096'},
                     'portion': 'General', 'compound': 'null', 'name': 'Coca-Cola', 'price': 75,
                     'code': 141, 'ordercode': 178, 'notable': 35, 'amount': 1, 'notes': '',
                     'companion': 'null'},
                    {'order': 250,
                     'owner': {'code': '1', 'extra': 'null', 'name': 'DataSER,SRL', 'document': '131353072'},
                     'portion': 'General', 'compound': 'null', 'name': 'De Camarones', 'price': 350, 'code': 115,
                     'ordercode': 153, 'notable': 35, 'amount': 1, 'notes': '', 'companion': 'null'},
                    {'order': 250, 'owner': {'code': '1', 'extra': 'null', 'name': 'Cuenta unica', 'document': 'null'},
                     'portion': 'General', 'compound': 'null', 'name': 'Blue Cobb Salad', 'price': 350,
                     'code': 64, 'ordercode': 103, 'notable': 35, 'amount': 1, 'notes': '', 'companion': 'null'},
                    {'order': 250, 'owner': {'code': '1', 'extra': 'null', 'name': 'Cuenta unica', 'document': 'null'},
                     'portion': 'Res', 'compound': 'null', 'name': 'Burrito', 'price': 780, 'code': 92, 'ordercode': 133,
                     'notable': 35, 'amount': 2,
                     'notes': '', 'companion': 'null'}],
       'rnc': '131353096'}
    print(EndPointHandle(d).msg)
__author__ = 'hidura'
