from sqlalchemy import Column, BIGINT, Text, MetaData, Table
from tools.DataBase.Connect import conection
from tools.DataBase.Definition.Base import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey

from tools.DataBase.Definition.Contact import Contact
from tools.DataBase.Definition.Status import Status


class Supplier(Base):
    metadata = MetaData()

    __tablename__ = "supplier_reg"

    __table_args__ = {"useexisting": True}

    id = Column("id", BIGINT, primary_key=True, autoincrement=True)
    code = Column("code", BIGINT, nullable=False, unique=True)
    contact = Column('contact', BIGINT, ForeignKey(Contact.code), nullable=True)
    status = Column('status', BIGINT, ForeignKey(Status.code), nullable=False, default=12)
    sup_name = Column("sup_name", Text, nullable=True)
    rnc = Column("rnc", Text, nullable=True)
    # Relationship
    status_rel_cmp = relationship(Status, backref=backref("Supplier"))
    contact_rel_cmp = relationship(Contact, backref=backref("Supplier"))

    def __repr__(self):
        return "<Supplier(id='%s',code='%s', contact='%s', status='%s', sup_name='%s', rnc='%s')>" \
               % (self.id, self.code, self.contact, self.status, self.sup_name, self.rnc)

    supplier_tbl = Table(__tablename__, metadata, id, code, contact, status, sup_name, rnc)

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
    Supplier()

__author__ = 'hidura'
