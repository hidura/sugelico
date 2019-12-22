from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.expression import and_

from tools.DataBase.CodeGenerator import CodeGen
from tools.DataBase.Connect import conection
from tools.DataBase.Definition.Level import Level
from tools.DataBase.Process import DBProcess
from tools.main.general import general


class LevelProc:
    def __init__(self):
        self.connORM = conection().conORM()

        self.status = 200
        self.msg = None
        self.type = "text/plain"
        Session = sessionmaker(bind=self.connORM)
        self.session = Session()

    def create(self, inputs):
        # This method will create an expense.
        self.code = CodeGen().GenCode({"table": Level.__tablename__, "column": Level.code.name})
        # Generating the code.
        self.session.add(Level(code=self.code, level_name=inputs["level_name"]))
        # Saving
        self.session.commit()
        self.session.close()
        self.connORM.dispose()
        return {"status": 200, "value": {Level.code.name: self.code}, 'type': 'application/json'}

    def Handle(self, inputs):
        # This method will modify an expanse.
        item = int(inputs[Level.code.name])
        storeDict = {}

        for column in DBProcess(Level.level_tbl).getColumnDefinition:
            if column["name"] in inputs:
                storeDict[column["expr"]] = inputs[column["name"]]

        self.session.query(Level).filter_by(code=item).update(storeDict)
        self.session.commit()
        self.session.close()
        self.connORM.dispose()

        return {"status": 200, "value": {Level.code.name: item}, 'type': 'application/json'}

    def Get(self, inputs):
        # This method gets the data, from the db.
        storeDict = []
        if Level.code.name in inputs:
            storeDict = self.session.query(Level). \
                filter(and_(Level.code == int(inputs[Level.code.name])))
        elif Level.level_name.name in inputs:
            storeDict = self.session.query(Level). \
                filter(and_(Level.level_name.like("%" + inputs[Level.level_name.name] + "%")))
        # The next area is in charge to extract the information,
        # from the store Dict and add it to the dataCol to be returned

        dataCol = []

        for dataLst in storeDict:

            dicStore = {"level_name": dataLst._asdict()["level_name"]}
            for key in DBProcess(Level.level_tbl).getColumnDefinition:

                dataDict = dataLst._asdict()[Level.__name__].__dict__  # Getting the dictionary of the list.
                colname = key["name"]  # Getting the column name.
                if "_sa_" not in colname:  # Just if the column name is on the dictionary, add it to the dictStore.
                    dicStore[colname] = dataDict[colname]

            dataCol.append(dicStore)
            # Appending everything to be returned

        self.session.close()
        self.connORM.dispose()
        return {"status": 200, "value": dataCol, 'type': 'application/json'}

if __name__ == '__main__':
    LevelProc().create({"level_name":"Tipo de pago"})

__author__ = 'hidura'
