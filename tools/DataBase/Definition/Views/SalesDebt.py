__maintainer__ = 'Diego Hidalgo'
__email__ = 'diego@sugelico.com'
__date__ = '7/2/2018'

from sqlalchemy import Column, BIGINT, Text, MetaData, Table
from sqlalchemy.dialects.mysql.base import NUMERIC
from sqlalchemy.sql.sqltypes import DateTime

from tools.DataBase.Definition.Base import Base

class SalesDebt(Base):
    def __init__(self, name):
        self.name = name

    __tablename__ = "sales_debt"
    metadata = MetaData()



    __table_args__ = {"useexisting": True}
    billid = Column("billid", BIGINT)
    billcode = Column('billcode', BIGINT)
    billncf = Column('billncf', BIGINT)
    billdate = Column('billdate', BIGINT)
    billuser = Column('billuser', BIGINT)
    billtime = Column('billtime', Text)
    billpaytp = Column('billpaytp', Text)

    billstatus = Column('billstatus', Text)
    billordertp = Column('billordertp', Text)
    billpreorder = Column('billpreorder', BIGINT,primary_key=True)
    billbilltp = Column('billbilltp', Text)

    billsubtotal = Column('billsubtotal', Text)
    billtax = Column('billtax', Text)
    billdisc = Column('billdisc', Text)

    billtotal = Column('billtotal', Text)
    billcashbox = Column('billcashbox', BIGINT)

    client_id = Column('client_id', Text)
    #client_name = Column('client_name', Text)

    ptpaid = Column('ptpaid', NUMERIC)

    SalesRep_tbl = Table(__tablename__, metadata, billid, billcode, billncf,
                         billdate, billtime, billpaytp, billstatus,
                         billordertp, billbilltp, billsubtotal, billtax, billdisc, billtotal,
                         billcashbox, ptpaid)

    def __Publish__(self):
        data={}
        for column in self.__table__.columns.keys():
            value=self.__dict__[self.__table__.columns[column].name]
            if self.__table__.columns[column].type =="BIGINT":
                data[self.__table__.columns[column].name]=int(value)
            elif self.__table__.columns[column].type =="Integer":
                data[self.__table__.columns[column].name]=int(value)

            elif self.__table__.columns[column].type=="NUMERIC":
                data[self.__table__.columns[column].name] = float(value)
            elif self.__table__.columns[column].type=="Decimal":
                data[self.__table__.columns[column].name] = float(value)

            elif self.__table__.columns[column].type=="time":
                data[self.__table__.columns[column].name] = str(value.strftime('%H:%M:%S'))
            elif self.__table__.columns[column].type=="datetime":
                data[self.__table__.columns[column].name] = str(value.strftime('%H:%M:%S'))
            else:
                data[self.__table__.columns[column].name] = str(value)
        return data