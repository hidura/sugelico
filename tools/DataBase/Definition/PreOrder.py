__maintainer__ = 'Diego Hidalgo'
__email__ = 'dhidalgo@codeservicecorp.com'
__date__ = '8/3/2018'

from sqlalchemy import Column, BIGINT, Text, MetaData, Table
from sqlalchemy.dialects.mysql.base import NUMERIC

from tools.DataBase.Connect import conection
from tools.DataBase.Definition.Base import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey
from tools.DataBase.Definition.Status import Status


class PreOrder(Base):
    metadata = MetaData()

    __tablename__ = "preorder_reg"

    __table_args__ = {"useexisting": True}

    id = Column('id', BIGINT, primary_key=True)
    code = Column("code", BIGINT, nullable=False)
    order_type = Column("order_type", BIGINT, nullable=False)
    created_by = Column("created_by", BIGINT, nullable=False)
    cashbox = Column("cashbox", BIGINT, nullable=False, default=1)
    created_date = Column("created_date", BIGINT, nullable=False)
    client = Column("client", BIGINT, nullable=False)
    cl_name = Column("cl_name", Text, nullable=False, default="GENERICO")
    rnc = Column("rnc", Text, nullable=False, default="0000000")
    _address = Column("_address", Text, nullable=True, default="")
    telephone = Column("telephone", Text, nullable=True, default="--")
    ncf_type = Column("ncf_type", Text, nullable=True, default="")
    total = Column("total", NUMERIC(20,2), nullable=False, default=0.00)
    current_credit = Column("current_credit", NUMERIC(20,2), nullable=True, default=0.00)
    credit = Column("credit", NUMERIC(20,2), nullable=True, default=0.00)
    max_credit = Column("max_credit", NUMERIC(20,2), nullable=True, default=0.00)
    status = Column("status", BIGINT, nullable=False)
    table_name = Column("table_name", Text, nullable=False, default="")
    table_code = Column("table_code", BIGINT, nullable=False, default=0)

    PreOrder_tbl = Table(__tablename__, metadata, id, code, order_type, created_by, created_date,
                         cashbox, client, cl_name, telephone, _address, rnc, ncf_type, total, current_credit,
                         credit,max_credit, status, table_name, table_code)

    def __repr__(self):
        return "<PreOrder(id='%s',code='%s',order_type='%s',created_by='%s',created_date='%s'," \
               "cashbox='%s',client='%s',cl_name='%s',telephone='%s',_address='%s',rnc='%s',ncf_type='%s'," \
               "total='%s',current_credit='%s',credit='%s',max_credit='%s',status='%s', table_name='%s'," \
               "table_code='%s')>" % \
               (self.id, self.code, self.order_type, self.created_by, self.created_date,self.cashbox,
                self.client, self.cl_name, self.telephone, self._address, self.rnc,self.ncf_type,
                self.total, self.current_credit, self.credit, self.max_credit, self.status,self.table_name,
                self.table_code)

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


if __name__ == '__main__':
    PreOrder()


