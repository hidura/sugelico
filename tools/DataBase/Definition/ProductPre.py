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


class ProductPre(Base):
    metadata = MetaData()

    __tablename__ = "productpre_reg"

    __table_args__ = {"useexisting": True}



    id = Column('id', BIGINT, primary_key=True)
    code=Column("code", BIGINT, nullable=False)
    product=Column("products", BIGINT, nullable=False)
    preorder=Column("preorder", BIGINT, nullable=False)
    product_name=Column("product_name", Text, nullable=False)
    amount = Column("amount", NUMERIC(20,2), default=0.00, nullable=False)
    notes = Column("notes", Text, nullable=True, default="")
    companion = Column("companion", Text, nullable=True, default="")
    term =Column("term", Text, nullable=True, default="")
    portion = Column("portion", Text, nullable=True, default="")
    subtotal=Column("subtotal", NUMERIC(20,2), default=0.00, nullable=False)
    tax=Column("tax", NUMERIC(20,2), default=0.00, nullable=False)
    total=Column("total", NUMERIC(20,2), default=0.00, nullable=False)
    discount=Column("discount", NUMERIC(20,2), default=0.00, nullable=False)
    status=Column("status", BIGINT, default=11, nullable=False)
    created_by = Column("created_by", BIGINT, nullable=False)
    cashbox = Column("cashbox", BIGINT, nullable=False, default=1)
    created_date = Column("created_date", BIGINT, nullable=False)
    client = Column("client", Text, nullable=False, default="GENERICO")

    ProductPre_tbl = Table(__tablename__, metadata, id, code,product, preorder,product_name,
                           amount,notes,companion,term,portion,subtotal,tax,total,discount,
                           status,created_by, cashbox,created_date,client)

    def __repr__(self):
        return "<ProductPre(id='%s',code='%s',product='%s',preorder='%s',product_name='%s'," \
               "amount='%s',notes='%s',companion='%s',term='%s',portion='%s',subtotal='%s'," \
               "tax='%s',total='%s',discount='%s',status='%s',created_by='%s',cashbox='%s'," \
               "created_date='%s',client='%s')>" % \
               (self.id, self.code, self.product,self.preorder, self.product_name,self.amount,
                self.notes,self.companion,self.term, self.portion,self.subtotal,self.tax,self.total,
                self.discount,self.status,self.created_by,self.cashbox,self.created_date,self.client)

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
    ProductPre()


