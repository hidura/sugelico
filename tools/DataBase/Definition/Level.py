from sqlalchemy import Column, BIGINT, Text, MetaData, Table
from tools.DataBase.Connect import conection
from tools.DataBase.Definition.Base import Base


class Level(Base):
    """The level of the type,
    means the classification of any
     type in the system."""

    metadata = MetaData(conection().conORM())

    __tablename__="level_reg"

    __table_args__ = {"useexisting": True}

    id = Column('id',BIGINT, primary_key=True)
    level_name = Column('lvl_name',Text, nullable=False)
    code = Column('code',BIGINT, nullable=False, unique=True)

    level_tbl = Table(__tablename__, metadata, id, level_name,code)




    def __repr__(self):
        return "<level_reg(id='%s', level_name='%s', " \
               "code='%s')>"%(self.id, self.level_name,
                              self.code)


    metadata.create_all()
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
    Level()


__author__ = 'hidura'
