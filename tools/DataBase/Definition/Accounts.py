from sqlalchemy import Column, BIGINT, Text, MetaData, Table
from sqlalchemy.dialects.mysql.base import NUMERIC

from tools.DataBase.Connect import conection
from tools.DataBase.Definition.Base import Base

class AccountsTbl(Base):
    metadata = MetaData()

    __tablename__ = "accounts_reg"

    __table_args__ = {"useexisting": True}

    id = Column('id', BIGINT, primary_key=True)
    code = Column("code", BIGINT, nullable=False)
    account_name = Column("account_name",Text, nullable=False)
    current_amount = Column("current_amount", NUMERIC(20, 2),
                            default=0.00, nullable=False)
    classification = Column("classification", Text, nullable=False)
    account_type = Column("account_type", Text, nullable=False)
    position = Column("position", Text)

    status = Column("status", BIGINT, nullable=False, default=11)
    Accounts_tbl = Table(__tablename__, metadata, id, code,
                         account_name, current_amount,
                         classification, account_type, position,status)

    def __repr__(self):
        return "<Accounts (id='%s', code='%s', " \
               "account_name='%s', current_amount='%s'," \
               "classification='%s',account_type='%s'," \
               "position='%s',status='%s')>" % \
               (self.id, self.code,
                self.account_name, self.current_amount,
                self.classification, self.account_type,
                self.position,self.status)

    engine = conection().conORM()
    metadata.create_all(engine)

    engine.connect().close()


if __name__ == '__main__':
    AccountsTbl()

__author__ = 'hidura'
