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


class ProductsMove(Base):
    metadata = MetaData()

    __tablename__ = "products_move_reg"

    __table_args__ = {"useexisting": True}

    id = Column('id', BIGINT, primary_key=True)
    code = Column('code', BIGINT, nullable=False)
    send_date = Column("send_date", BIGINT, nullable=True)
    created_by=Column("created_by", BIGINT, nullable=True)
    created = Column("created", BIGINT, nullable=True)
    notes = Column("notes", Text, nullable=True)
    from_warehouse = Column("from_warehouse", Text, nullable=True)
    to_warehouse = Column("to_warehouse", Text, nullable=True)

    ProductsMove_tbl = Table(__tablename__, metadata, id, code, send_date,
                             created_by, created, notes, from_warehouse, to_warehouse)

    def __repr__(self):
        return "<ProductsMove(id='%s', code='%s',send_date='%s'," \
               "created_by='%s',created='%s',notes='%s',from_warehouse='%s'," \
               "to_warehouse='%s')>" % \
               (self.id, self.code, self.send_date,
                self.created_by, self.created, self.notes,
                self.from_warehouse, self.to_warehouse)

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
    ProductsMove()


