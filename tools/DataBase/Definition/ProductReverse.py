import datetime

from sqlalchemy import Column, BIGINT, Text, MetaData, Table
from sqlalchemy.dialects.postgresql.base import TIME

from tools.DataBase.Connect import conection
from tools.DataBase.Definition.Base import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey
from tools.DataBase.Definition.Status import Status

from sqlalchemy.sql.sqltypes import DateTime

class ProductReverse(Base):
    metadata = MetaData()
    __tablename__ = "productreverse_reg"

    __table_args__ = {"useexisting": True}

    id = Column('id', BIGINT, primary_key=True)
    code = Column("code", BIGINT, nullable=False)
    created_by = Column('created_by', BIGINT, nullable=False)
    created_date = Column('created_date', BIGINT, nullable=False)
    _time = Column("_time", DateTime(timezone=True), nullable=True, onupdate=datetime.datetime.now)
    preorder = Column("preorder", BIGINT, nullable=False)
    product = Column("product", BIGINT, nullable=False)
    reason = Column("reason", Text, nullable=False)
    status = Column("status", BIGINT, nullable=False, default=16)

    ProductReverse_tbl = Table(__tablename__, metadata,
                               id, code, created_by,
                               created_date, _time,
                               preorder, reason, status)

    def __repr__(self):
        return "<ProductReverse (id='%s', code='%s', created_by='%s', " \
               "created_date='%s', _time='%s', preorder='%s', reason='%s', status='%s')>" % \
               (self.id, self.code, self.created_by,
                self.created_date, self._time, self.preorder, self.reason, self.status)

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
    ProductReverse()

__author__ = 'hidura'
