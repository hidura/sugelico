from sqlalchemy import Column, BIGINT, Text, MetaData, Table
from sqlalchemy.dialects.mysql.base import NUMERIC
from sqlalchemy.dialects.postgresql.base import TIME

from tools.DataBase.Connect import conection
from tools.DataBase.Definition.Base import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey
from tools.DataBase.Definition.Status import Status


class HappyHour(Base):
    metadata = MetaData()

    __tablename__ = "happyhour_reg"

    __table_args__ = {"useexisting": True}

    id = Column('id', BIGINT, primary_key=True)
    code=Column("code", BIGINT, nullable=False)
    product = Column('product', BIGINT, nullable=False)
    discount = Column('discount', NUMERIC(20,2), nullable=False, default=0.00)
    start_hour=Column("start_hour", TIME, nullable=False)
    end_hour=Column("start_hour", TIME, nullable=False)
    status=Column("status", BIGINT, nullable=False)
    days=Column("days", Text, nullable=False)
    Discount_tbl = Table(__tablename__, metadata, id, product, discount, start_hour,
                         end_hour, status, days, code)

    def __repr__(self):
        return "<HappyHour (id='%s', product='%s', discount='%s', " \
               "start_hour='%s', end_hour='%s', days='%s', code='%s')>" % \
               (self.id, self.product, self.discount,
                self.start_hour, self.end_hour, self.days,self.code)

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
    HappyHour()

__author__ = 'hidura'
