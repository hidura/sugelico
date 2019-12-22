from sqlalchemy import Column, BIGINT, Text, MetaData, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey
from tools.DataBase.Connect import conection
from tools.DataBase.Definition.Base import Base
from tools.DataBase.Definition.Type import Type


class Status(Base):
    metadata = MetaData()

    __tablename__ = "status_reg"

    __table_args__ = {"useexisting": True}

    id = Column('id', BIGINT, primary_key=True)
    description = Column('description', Text, nullable=False)
    statustp = Column('statustp', BIGINT,ForeignKey(Type.code), nullable=False)
    code = Column('code', BIGINT, nullable=False, unique=True)

    Status_tbl = Table(__tablename__, metadata, id, description, statustp, code)


    #Relations
    table_rel_typ = relationship(Type, backref=backref("Status"))


    def __repr__(self):
        return "<Status (id='%s', description='%s', statustp='%s', code='%s')>" % \
               (self.id, self.description, self.statustp, self.code)

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
    Status()

__author__ = 'hidura'



if __name__ == '__main__':
    Status()

__author__ = 'hidura'
