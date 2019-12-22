from sqlalchemy import Column, BIGINT, Text, MetaData, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey
from tools.DataBase.Definition.Base import Base
from tools.DataBase.Definition.Status import Status
from tools.DataBase.Definition.company import company


class Branch(Base):
    metadata = MetaData()
    __tablename__ = "branch_reg"

    __table_args__ = {"useexisting": True}

    id = Column('id', BIGINT, primary_key=True)
    _name = Column('_name', Text, nullable=True)
    _address = Column('_address', Text, nullable=False)
    telephone = Column('telephone', Text, nullable=True)
    code = Column('code', BIGINT, nullable=True, unique=True)
    status = Column('status', BIGINT, ForeignKey(Status.code), default=12, nullable=False)
    company = Column('company', BIGINT, ForeignKey(company.code), nullable=True)
    image = Column("image", Text)
    altpath = Column("altpath", Text)

    def __repr__(self):
        return "<Branch (id='%s', _name='%s', code='%s', status='%s', " \
               "_address='%s', telephone='%s', type='%s', image='%s',company='%s',altpath='%s')>" \
               % (self.id, self._name, self.code, self.status,
                  self._address, self.telephone, self.type, self.image, self.company, self.altpath)

    branch_tbl = Table(__tablename__, metadata, id, _name, code, status,
                       _address, telephone, image, company, altpath)


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
    Branch()

__author__ = 'hidura'
