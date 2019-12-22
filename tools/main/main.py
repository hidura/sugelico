# -*- coding: utf8 -*-
'''
Created on Jun 24, 2013

@author: hidura
'''
import sys
import urllib.parse

from mongoengine import connect

from tools.main.process.Accounting import Accounting
from tools.main.process.Accounts import Accounts
from tools.main.process.Bills import Bills
from tools.main.process.Categories import Categories
from tools.main.process.Clients import Clients
from tools.main.process.General import General
from tools.main.process.Items import Items
from tools.main.process.Level import LevelProc
from tools.main.process.Recepie import Recepie
from tools.main.process.Status import StatusProc
from tools.main.process.Table import Table
from tools.main.process.Types import Types
from tools.main.process.Warehouse import warehouse
from tools.main.process.login import login
from tools.main.process.manContact import ManContact
from tools.main.process.supplier import supplier
from tools.main.process.TableArea import TableArea

from .general import general
from tools.DataBase.Connect import conection
from tools.main.process.Company import Company


class main:
    connORM = conection().conORM()

    def __init__(self, inputs, environ):
        from tools.Utilities import getNewPage
        self.getPage = getNewPage
        self.callObjects(inputs, environ)

    def callObjects(self, inputs, environ):
        self.result = ""
        inputs["__documentroot__"]=environ["DOCUMENT_ROOT"]
        if "md" in inputs:

            self.result = {"status":200,
                                  "value": self.getPage(inputs["md"], inputs, environ).getResult(),
                                  "type":"text/html"
                                  }
        elif "classname" in inputs and "md" not in inputs:

            codeName = inputs["classname"]
            inputs.pop("classname", None)
            self.result = self.exec_code(codeName, inputs, environ)


    def getResult(self):

        return self.result

    def exec_code(self, codeName, inputs, environ):
        method_class = codeName.split(".")[0]
        method = codeName.split(".")[1]

        self.connODM = conection().conODM()
        ClsPckg = {"general":general, "Company":Company,
                   "General":General, "login":login, "ManContact":ManContact,
                   "Accounting":Accounting, "Bills":Bills, "Items":Items,
                   "Accounts":Accounts,"WareHouse":warehouse,
                   "Clients":Clients,"Recepie":Recepie, "supplier":supplier,
                   "Table":Table, "TableArea":TableArea,"Types":Types,
                   "Level":LevelProc, "Status":StatusProc, "Categories":Categories}


        retVal = getattr(ClsPckg[method_class](), method)(inputs)

        return retVal