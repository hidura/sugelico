from sqlalchemy import Column, BIGINT, Text, MetaData, Table
from sqlalchemy.dialects.mysql.base import NUMERIC

from tools.DataBase.Connect import conection
from tools.DataBase.Definition.Base import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey
from tools.DataBase.Definition.Status import Status


class AccountsTbl(Base):
    metadata = MetaData()

    __tablename__ = "accounts_reg"

    __table_args__ = {"useexisting": True}

    id = Column('id', BIGINT, primary_key=True)
    code = Column("code", BIGINT, nullable=False)
    account_name = Column("account_name",Text, nullable=False)
    current_amount = Column("current_amount", NUMERIC(20, 2),
                            default=0.00, nullable=False)

    acc_type = Column("acc_type", BIGINT, nullable=True)

    status = Column("status", BIGINT, nullable=True, default=11)

    Accounts_tbl = Table(__tablename__, metadata, id, acc_type, code,
                         account_name, current_amount, status)

    def __repr__(self):
        return "<Accounts (id='%s', code='%s', " \
               "account_name='%s', current_amount='%s', " \
               "acc_type='%s', status='%s')>" % \
               (self.id, self.code,
                self.account_name, self.current_amount, self.acc_type, self.status)

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
    AccountsTbl()

__author__ = 'hidura'
