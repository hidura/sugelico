__maintainer__ = 'Diego Hidalgo'
__email__ = 'dhidalgo@codeservicecorp.com'
__date__ = '4/22/2018'

from sqlalchemy import Column, BIGINT, Text, MetaData, Table
from sqlalchemy.dialects.mysql.base import NUMERIC

from tools.DataBase.Connect import conection
from tools.DataBase.Definition.Base import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey
from tools.DataBase.Definition.Status import Status


class ProductsAmount(Base):
    metadata = MetaData()

    __tablename__ = "products_amount_asc"

    __table_args__ = {"useexisting": True}

    id = Column('id', BIGINT, primary_key=True)
    warehouse =Column("warehouse", BIGINT, nullable=True)
    product = Column("product", BIGINT, nullable=True)
    amount = Column("amount", NUMERIC(20,2), nullable=True)

    ProductsAmount_tbl = Table(__tablename__, metadata, id, warehouse, product, amount)

    def __repr__(self):
        return "<ProductsAmount(id='%s', product='%s', amount='%s', warehouse='%s')>" % \
               (self.id, self.product, self.amount, self.warehouse)

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
    ProductsAmount()


