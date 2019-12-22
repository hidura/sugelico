from sqlalchemy import Column, BIGINT, Text, MetaData, Table
from tools.DataBase.Connect import conection
from tools.DataBase.Definition.Base import Base


class category(Base):
    metadata = MetaData()

    __tablename__ = "category_reg"

    __table_args__ = {"useexisting": True}

    id = Column('id', BIGINT, primary_key=True)
    cat_name = Column('cat_name', Text, nullable=False)
    code = Column("code", BIGINT, nullable=False, unique=True)
    status = Column("status", BIGINT, nullable=False, default=11)
    cat_type = Column("cat_type", BIGINT, nullable=True, default=63)
    print_time = Column("print_time", BIGINT, nullable=True, default=0)
    company = Column("company", BIGINT, nullable=True, default=0)
    printer = Column("printer", Text, nullable=True, default='')
    type_product = Column("type_product", BIGINT, nullable=True, default=131)# This area will add to the category the
    # property to check if the product is: Liquid, solid or something like that,
    # also can be used to mark drinks, juices, etc.
    avatar = Column("avatar", Text, nullable=True, default="")
    tp_avatar = Column("tp_avatar", Text, nullable=True, default="")
    category_tbl = Table(__tablename__, metadata, id, cat_name,
                         status, avatar, code, cat_type, type_product, tp_avatar,
                         printer, print_time, company)

    def __repr__(self):
        return "<category (id='%s', cat_name='%s', status='%s', avatar='%s', " \
               "code='%s', cat_type='%s', type_product='%s'tp_avatar='%s', " \
               "printer='%s', print_time='%s',company='%s')>" % \
               (self.id, self.cat_name, self.status, self.avatar,
                self.code, self.cat_type,self.type_product,self.tp_avatar,
                self.printer, self.print_time, self.company)

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
    category()

__author__ = 'hidura'
