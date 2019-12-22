from mongoengine.connection import disconnect
import json
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.expression import select

from tools.DataBase.CodeGenerator import CodeGen
from tools.DataBase.Connect import conection
from tools.DataBase.Definition.Level import Level
from tools.DataBase.Definition.Status import Status
from tools.DataBase.Definition.Type import Type
from tools.DataBase.Definition.company import company
from tools.DataBase.ODM.DataModelODM import Country, Equivalence, cashbox_open, cashbox, printer_reg, sysrules, \
    rule_user

from tools.DataBase.ODM.internal import Label, LabelValue, Language
from tools.DataBase.Process import DBProcess
from tools.main.general import general

# import astropy.time as astime
# from astropy.time import Time
from datetime import datetime

class General:
    def __init__(self):
        self.connORM = conection().conORM()

        self.status = 200
        self.msg = None
        self.type = "text/plain"
        Session = sessionmaker(bind=self.connORM)
        self.session = Session()


    def date2julian(self, inputs):
        gdate=inputs["date"]
        if gdate == None:
            gdate = datetime.now()
        else:
            if len(str(gdate).split(" "))>0:
                _gdate = str(gdate).split(" ")[0]
                gdate=_gdate
            else:
                _gdate = gdate
            if "/" in _gdate:
                dateLst=_gdate.split("/")
                if len(dateLst[2])==4:
                    gdate=datetime.strptime(_gdate.split("/")[2]+"/"+_gdate.split("/")[1]+"/"+_gdate.split("/")[0], '%Y/%m/%d')
        return {"status": 200, "value": float(astime.Time(gdate).jd), 'type': 'application/json'}

    def julian2date(self, inputs):
        jdate=inputs["date"]
        td_j = Time(float(jdate), format='jd', scale='utc')
        return {"status": 200, "value": td_j.iso, 'type': 'application/json'}

    def getStatus(self, inputs):
        status_data=self.session.execute(select([Status.code, Status.name]).
                                      where(Status.tp_status==int(inputs[Status.tp_status.name])))
        data = status_data.fetchall()

        if "datatype" in inputs:
            if inputs["datatype"]=="json":
                self.type="application/json"
                self.msg ={}

        else:
            self.type="text/html"
            self.msg=""

        if self.type=="text/html":
            for piece in data:
                self.msg+="<option value='"+str(piece[0])+"'>"+str(piece[1])+"</option>"

        elif self.type=="application/json":
            self.msg ={}
            for piece in data:
                self.msg[str(piece[0])]=str(piece[1])
        self.session.close()
        self.connORM.dispose()

        return {"status":200, "value":self.msg, "type":self.type}

    def getType(self, inputs):
        types_data=self.session.query(Type.code, Type.name).\
            filter(Type.level==int(inputs[Type.level.name]))
        typesLst =[]
        for piece in types_data:
            typesLst.append({str(piece.code):piece.name})
        self.session.close()

        self.connORM.dispose()
        return {"status":200, "value":typesLst, "type":"application/json"}

    def level(self, inputs):
        code =0
        if "code" not in inputs:
            code =CodeGen().GenCode({"table":Level.__tablename__,
                                     "column":Level.code.name})
            self.session.add(Level(code=code, name=inputs[Level.name.name]))
        else:
            code=int(inputs["code"])
            self.session.query(Level).filter_by(code=code).update({Level.name:inputs[Level.name.name]})

        self.session.commit()
        self.session.close()
        self.connORM.dispose()
        return {"status":200, "value":{Level.code.name:code}, "type":"application/json"}

    def _type(self, inputs):
        code = 0
        if Type.code.name not in inputs:
            code = CodeGen().GenCode({"table": Type.__tablename__,
                                      "column": Type.code.name})
            self.session.add(Type(level=int(inputs["level"]), code=code, name=inputs[Type.name.name]))
        else:
            code = int(inputs[Type.code.name])
            self.session.query(Type).filter_by(code=code).update({Type.name: inputs[Type.name.name],
                                                                  Type.level:int(inputs[Type.code.name])})

        self.session.commit()
        self.session.close()
        self.connORM.dispose()
        return {"status": 200, "value": {Type.code.name: code}, "type": "application/json"}


    def addRule(self, inputs):
        rulename=inputs["rule_name"]
        description=inputs["description"]
        code = CodeGen().GenCode({"table": 'sysrules',
                                  "column": "code"})
        sysrules(code=code, name=rulename, description=description).save()
        ruleuserslst = []
        users = json.loads(inputs["users"])
        for user in users:
            ruleuserslst.append(rule_user(
                user_code=user, rule_code=code, rule_name=rulename))
        if len(ruleuserslst) > 0:
            rule_user.objects.insert(ruleuserslst)

        self.session.commit()
        self.session.close()
        self.connORM.dispose()
        return {"status": 200, "value": {"code": code}, "type": "application/json"}

    def getRule(self, inputs):

        if "user" in inputs:
            self.msg=json.dumps(rule_user.objects(user_code=int(inputs["user"])))
        elif "rule" in inputs:
            self.msg = [json.loads(rule_user.objects(rule_code=int(inputs["rule"])).to_json()),
                        json.loads(sysrules.objects(code=int(inputs["rule"])).to_json())]
        else:
            self.msg = [json.loads(sysrules.objects().to_json())]
        self.session.commit()
        self.session.close()
        self.connORM.dispose()
        return {"status": 200, "value": self.msg, "type": "application/json"}


    def modRule(self, inputs):
        rulename=inputs["rule_name"]
        description=inputs["description"]
        code = int(inputs["code"])
        sysrules.objects(code=code).update(set__name=rulename, set__description=description)
        ruleuserslst = []
        rule_user.objects(rule_code=code).delete()
        users = json.loads(inputs["users"])
        for user in users:
            ruleuserslst.append(rule_user(
                user_code=user, rule_code=code, rule_name=rulename))
        if len(ruleuserslst) > 0:
            rule_user.objects.insert(ruleuserslst)

        self.session.commit()
        self.session.close()
        self.connORM.dispose()
        return {"status": 200, "value": {"code": code}, "type": "application/json"}


    """Label"""
    #Creation
    def createLabel(self, inputs):
        #This mehtod will create a new label that can be add to a button or a label, span, etc.
        if "name" in inputs and "value" in inputs:
            label_info=Label(name=inputs["name"], value=inputs["value"]).save()
            self.msg={"code":label_info.id}

        else:
            self.msg={"error":"Alguno de los valores no esta presente"}

        self.session.close()
        self.connORM.dispose()
        return {"status": 200, "value": self.msg, "type": "application/json"}

    #Getting
    def getLabelBy(self, inputs):
        # This mehtod will create a new label that can be add to a button or a label, span, etc.
        self.msg = []
        if "name" in inputs:
            datalst = Label.objects(name__contains=inputs["name"])
            for piece in datalst:
                self.msg.append({"code": piece.id, "name": piece.name, "value": piece.value})
        elif "id" in inputs:
            datalst = Label.objects(id=inputs["id"])
            for piece in datalst:
                self.msg.append({"code": piece.id, "name": piece.name, "value": piece.value})
        else:
            self.msg.append({"error": "Alguno de los valores no esta presente"})

        self.session.close()
        self.connORM.dispose()
        return {"status": 200, "value": self.msg, "type": "application/json"}

    #Translating
    def addLabelLang(self, inputs):
        # This mehtod will create a new traduction for a label.
        if "label" in inputs and "value" in inputs and "language" in inputs:
            label_info = LabelValue(label=inputs["name"], value=inputs["value"], language=inputs["language"]).save()
            self.msg = {"code": label_info.id}
        else:
            self.msg = {"error": "Alguno de los valores no esta presente"}

        self.session.close()
        self.connORM.dispose()
        return {"status": 200, "value": self.msg, "type": "application/json"}


    """Language"""
    #Creating
    def addLanguage(self, inputs):
        # This mehtod will create a new language.
        if "name" in inputs and "code" in inputs:
            label_info = Language(name=inputs["name"], value=inputs["value"], language=inputs["language"]).save()
            self.msg = {"code": label_info.id}
        else:
            self.msg = {"error": "Alguno de los valores no esta presente"}

        self.session.close()
        return {"status": 200, "value": self.msg, "type": "application/json"}

    #Getting
    def getLangBy(self, inputs):
        # This mehtod will create a new label that can be add to a button or a label, span, etc.
        self.msg = []
        if "name" in inputs:
            datalst = Language.objects(name__contains=inputs["name"])
            for piece in datalst:
                self.msg.append({"code": piece.id, "name": piece.name, "domain": piece.code})
        elif "id" in inputs:
            datalst = Language.objects(id=inputs["id"])
            for piece in datalst:
                self.msg.append({"code": piece.id, "name": piece.name, "domain": piece.code})
        else:
            self.msg.append({"error": "Alguno de los valores no esta presente"})

        self.session.close()
        self.connORM.dispose()
        return {"status": 200, "value": self.msg, "type": "application/json"}


    def getCountry(self, inputs):
        countryLst =[]
        country = Country.objects()
        for piece in country:
            countryLst.append({"name":piece.name, "code":piece.code})


        self.session.close()
        self.connORM.dispose()
        return {"status": 200, "value": countryLst, "type": "application/json"}


    def WrapInfo(self, inputs, data, field_names):
        dataInfo = []
        wrap_to = inputs["wrap_to"]
        for piece in data:
            fields_data ={}
            for fields in field_names:
                key = list(fields.keys())[0]
                if key in piece:
                    fields_data[fields[key]] = piece[key]

            dataInfo.append(fields_data)

        self.session.close()
        self.connORM.dispose()
        return {"results":dataInfo}


    def getFilters(self, inputs, storeDict, table):
        # In developing, this method will create all the filters for the table.
        for key in DBProcess(table).getColumnDefinition:
            if key["name"] in inputs:

                if len(inputs[key["name"]].split("=")) > 1:
                    comparison = inputs[key["name"]].split("=")[0]
                    data = DBProcess(table.Item_tbl).parse(key, inputs[key["name"]].split("=")[1])
                    if comparison == "__gte":
                        storeDict = storeDict.filter(key["expr"] >= data)
                    elif comparison == "__lte":
                        storeDict = storeDict.filter(key["expr"] <= data)

                    elif comparison == "__gt":
                        storeDict = storeDict.filter(key["expr"] > data)
                    elif comparison == "__lt":
                        storeDict = storeDict.filter(key["expr"] < data)
                    elif comparison == "__eq":
                        storeDict = storeDict.filter(key["expr"] == data)
                    elif "__ilike" in comparison or "__like" in comparison:
                        likeStrPre = ""
                        likeStrEnd = ""

                        if data[0] == "%":
                            likeStrPre = data[0]
                            data = data[0:]

                        if data[len(data) - 1] == "%":
                            likeStrEnd = data[len(data) - 1]
                            data = data[len(data) - 1]
                        if comparison == "__ilike":
                            storeDict = storeDict.filter(key["expr"].ilike(likeStrPre + str(data).lower() + likeStrEnd))
                        elif comparison == "__like":
                            storeDict = storeDict.filter(key["expr"].ilike(likeStrPre + str(data) + likeStrEnd))
        self.session.close()
        self.connORM.dispose()
        return storeDict


    def getInputs(self, inputs):
        self.session.close()
        self.connORM.dispose()
        return {"status": 200, "value": str(inputs), "type": "application/json"}

    def getEquivalence(self, inputs):
        # Method that extract the equivalence list
        if "from_eq" in inputs:
            equivalence=int(inputs["from_eq"])

        dataCol = Equivalence.objects(from_eq=equivalence)

        self.msg=[]
        for piece in dataCol:

            tpname = self.session.query(Type.tpname).filter_by(code=piece.to_eq).first()
            if tpname !=None:
                self.msg.append({"tpname": tpname,
                             "code":piece.code, "operation":piece.optype, "amount":piece.equivalence,
                             "name":piece.eq_name})

        self.session.close()
        self.connORM.dispose()
        return {"status": 200, "value": self.msg, "type": "application/json"}

    def getCashBox(self, inputs):
        cashbox_id = "001"
        if "cashbox" in inputs:
            cashbox_id = inputs["cashbox"]

        cashbox_info = cashbox.objects(_name=cashbox_id, status=11)
        self.session.close()
        self.connORM.dispose()

        if cashbox_info.first() !=None:
            return cashbox_info.first().code


    # This method is to extract the Business Header, for bills and legal documents.
    def getBusinessHeader(self, inputs):
        cmpInfo=self.session.query(company)
        if "company" in inputs:
            cmpInfo = cmpInfo.filter(company.code == int(inputs["company"]))

        data = cmpInfo.first()
        if data !=None:
            self.msg={company.code.name:cmpInfo.code,
                      company._name.name: cmpInfo._name,
                      company.address.name: cmpInfo.address,
                      company.telephone.name: cmpInfo.telephone,
                      company.image.name: cmpInfo.image,
                      company.rnc.name: cmpInfo.rnc}



    def HandlePrinter(self, inputs):
        # First creating or taking the code of the printer
        printer_obj = None
        brand = ""
        model = ""
        server = ""
        path = ""
        username = ""
        password = ""
        _type = ""
        status = 11
        name = ""

        if "code" in inputs:
            code = int(inputs["code"])
            printer_obj = printer_reg.objects(code=code).first()
            if printer_obj!=None:
                brand=printer_obj.brand
                model=printer_obj.model
                server=printer_obj.server
                path=printer_obj.path
                username=printer_obj.username
                password=printer_obj.password
                _type=printer_obj._type
                status=printer_obj.status
                name=printer_obj.name
        else:
            code = CodeGen().GenCode({"table": "printer_reg",
                                      "column": "code"})
            printer_reg(code=code, company=inputs["company"]).save()

        if "name" in inputs:
            name = inputs["name"]

        if "brand" in inputs:
            brand=inputs["brand"]

        if "model" in inputs:
            model=inputs["model"]

        if "server" in inputs:
            server=inputs["server"]

        if "password" in inputs:
            password=inputs["password"]

        if "_type" in inputs:
            _type=inputs["_type"]

        if "status" in inputs:
            status=int(inputs["status"])

        if "path" in inputs:
            path=str(inputs["path"])

        if "username" in inputs:
            username=str(inputs["username"])



        category=""
        if "category" in inputs:
            category=inputs["category"]
        printer_reg.objects(code=code).\
            update(set__brand=brand, set__model=model,
                   set__server=server, set__path=path,
                   set__username=username, set__password=password,
                   set___type=_type, set__category=category,
                   set__status=status, set__name=name)

        self.session.close()
        self.connORM.dispose()

        return {"status": 200, "value": code, "type": "application/json"}


    def getPrinters(self, inputs):
        self.msg = []
        if "company" in inputs:
            self.msg= printer_reg.objects(company=int(inputs["company"])).to_json()

        elif "brand" in inputs:
            self.msg = printer_reg.objects(brand__icontains=inputs["brand"]).to_json()

        return {"status": 200, "value": self.msg, "type": "text/plain"}


if __name__ == '__main__':
    # product_type=[{"name":"Insumo","level":9},
    #               {"name": "Producto", "level": 9},
    #               {"name": "Otros", "level": 9}]
    # for piece in product_type:
    #     print(General()._type(piece))
    print(General().getCashBox({"cashbox":"001"}))
    #print(General().manTablet({"brand":1, "model":1, "imei":"353439062232007", "company":6}))

__author__ = 'hidura'
