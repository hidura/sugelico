from sqlalchemy import Column, BIGINT, Text, MetaData, Table
from tools.DataBase.Connect import conection
from tools.DataBase.Definition.Base import Base


class requisition(Base):
    metadata = MetaData()

    __tablename__ = "requisition_reg"

    __table_args__ = {"useexisting": True}

    id = Column('id', BIGINT, primary_key=True)
    code = Column("code", BIGINT, unique=True, nullable=False)
    created_by = Column("created_by", BIGINT, nullable=True)
    created = Column("created", BIGINT, nullable=True)
    description = Column("description", Text, nullable=True)
    status = Column("status", BIGINT, nullable=True)
    Requisition_tbl = Table(__tablename__, metadata, id, code, description, created_by, created, status)

    def __repr__(self):
        return "<Requisition (id='%s', code='%s', " \
               "created_by='%s',created='%s', status='%s',descriptio='%s')>" % \
               (self.id, self.code, self.created_by,
                self.created, self.status, self.description)



if __name__ == '__main__':
    requisition()

__author__ = 'hidura'
