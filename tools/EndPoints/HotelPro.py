import io
import json

from urllib import request


import requests
from sqlalchemy.orm.session import sessionmaker

from tools.DataBase.Connect import conection
#from tools.DataBase.Definition.Products import Products
#from tools.main.process.General import General
#from tools.main.process.ResTable import ResTable
from tools.main.process.Product import Product


class HotelPro:
    def __init__(self):
        self.connODM = conection().conODM()
        self.connORM = conection().conORM()

        self.status = 200
        self.msg = None
        self.type = "text/plain"
        Session = sessionmaker(bind=self.connORM)
        self.session = Session()


    def process(self, inputs):
        #Creating the products params.
        detailProd=[]
        invited=1
        rnc = inputs["rnc"]
        past_rnc=[rnc]
        for piece in inputs["products"]:

            productInfo=Product().getProductInformation({"product":int(piece["code"])})
            portions= productInfo["value"]["portions"]
            syscode=productInfo["value"]["syscode"]
            for subPortion in portions.split(","):
                if piece["portion"] == subPortion.split(":")[1] and int(subPortion.split(":")[0])>0:
                    syscode=subPortion.split(":")[0]


            if inputs["rnc"] != piece["owner"]["document"] and piece["owner"]["document"] not in past_rnc:
                invited +=1
                past_rnc.append(piece["owner"]["document"])

            raw_total=int(piece["total"])/int(piece["amount"])
            detailProd.append({"item":int(syscode),
                               "cantidad":piece["amount"],
                               "comentario":piece["notes"],
                               "invitado":invited,
                               "precio":raw_total})

        if rnc=="null" or rnc==None:
            rnc=""

        params = {"localid":int(inputs["company"]),
                  "mesa":int(inputs["table"]),
                  "rnc":rnc,
                  "invitado":1,
                  "vendedor":inputs["password"],
                  "odetalle":detailProd}

        url = 'http://aladino.dvrdns.org:3300/bprestservices/PedidoSugelico.rsvc?pedido='
        #url="http://test1.conceptoslogicos.com/bprestservices/PedidoSugelico.rsvc?pedido="
        response = requests.get(url+str(params))

        server_response = response.content

        message = None
        if "errors" in server_response.decode():
            message = json.loads(server_response.decode())["errors"][0]
        else:
            message = server_response.decode()
        self.status = response.status_code
        self.msg = message
        self.type = "text/plain"
        return {"status": response.status_code, "value":message, "type":self.type}




if __name__ == '__main__':
    dataCol={'table': 319, 'products':
        [{'order': 0, 'notable': 59, 'total': 75, 'portion': 'General',
          'name': 'Coca-Cola', 'owner': {'name': 'CodeService, SRL', 'rnc': '1-3135309-6',
                                         'extra': 'null', 'code': '1'}, 'price':100,
          'ordercode': 178, 'notes': '', 'amount': 1, 'code': 141, 'compound': 'null',
          'companion': 'null'},
         {'order': 0, 'notable': 35, 'total': 350, 'portion': 'General', 'price':500,
          'name': 'De Camarones', 'owner': {'name': 'Cuenta unica', 'rnc': '',
                                            'extra': 'null', 'code': '1'}, 'ordercode': 153,
          'notes': '', 'amount': 1, 'code': 115, 'compound': 'null', 'companion': 'null'},
         {'order': 0, 'notable': 35, 'total': 350, 'portion': 'General', 'price':250, 'name': 'Blue Cobb Salad',
          'owner': {'name': 'WebService, SRL', 'rnc': '130820724', 'extra': 'null', 'code': '1'},
          'ordercode': 103, 'notes': '', 'amount': 1, 'code': 64, 'compound': 'null', 'companion': 'null'},
         {'order': 0, 'notable': 35, 'total': 780, 'portion': 'Res', 'price':450, 'name': 'Burrito',
          'owner': {'name': 'Cuenta unica', 'rnc': 'null', 'extra': 'null', 'code': '1'},
          'ordercode': 133, 'notes': '', 'amount': 2, 'code': 92, 'compound': 'null', 'companion': 'null'}
         ], 'company': 2, 'rnc': {"rnc":'1-3135309-6', "nombre":"CodeService, SRL"}}

    print(HotelPro().process(dataCol))

__author__ = 'hidura'
