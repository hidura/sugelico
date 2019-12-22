__maintainer__ = 'Diego Hidalgo'
__email__ = 'diego@sugelico.com'
__date__ = '1/28/2018'

from sqlalchemy import Column, BIGINT, Text, MetaData, Table
from sqlalchemy.dialects.mysql.base import NUMERIC

from tools.DataBase.Connect import conection
from tools.DataBase.Definition.Base import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey
from tools.DataBase.Definition.Status import Status


class GetProducts(Base):
    def __init__(self, name):
        self.name = name
    metadata = MetaData()

    __tablename__ = "getproducts"

    __table_args__ = {"useexisting": True}

    item_reg_item_id= Column('item_reg_item_id', BIGINT, primary_key=True)
    item_name = Column('item_name', Text)
    code= Column('code', BIGINT)
    price = Column('price', Text)
    item_reg_status = Column('item_reg_status', BIGINT)
    category=Column('category', BIGINT)
    status_reg_description = Column('status_reg_description', Text)
    type_reg_tpname = Column('type_reg_tpname', Text)
    item_reg_item_type= Column('item_reg_item_type', BIGINT)
    subtotal = Column('subtotal', Text)
    tax = Column('tax', Text)
    cat_name= Column('cat_name', Text)
    cat_typename= Column('cat_typename', Text)

    printer= Column('printer', Text)
    category_reg_avatar= Column('category_reg_avatar', Text)
    category_reg_cat_type= Column('category_reg_cat_type', BIGINT)
    category_reg_status = Column('category_reg_status', BIGINT)
    category_code = Column('category_code', BIGINT)

    type_product= Column('type_product', BIGINT)
    item_reg_avatar= Column('item_reg_avatar', Text)
    tp_avatar= Column('tp_avatar', Text)


    GetProducts_tbl = Table(__tablename__, metadata, item_reg_item_id,item_name, code,price,
                            item_reg_status,category,status_reg_description,type_reg_tpname,item_reg_item_type,
                            subtotal,tax,cat_name,printer,category_reg_avatar,
                            category_reg_cat_type,type_product,item_reg_avatar,tp_avatar,
                            category_reg_status,cat_typename)



    engine = conection().conORM()
    metadata.create_all(engine)

    engine.connect().close()

    def __Publish__(self):
        data = {}
        for column in self.__table__.columns.keys():
            value = self.__dict__[self.__table__.columns[column].name]
            if self.__table__.columns[column].type == "BIGINT":
                data[self.__table__.columns[column].name] = int(value)
            elif self.__table__.columns[column].type == "Integer":
                data[self.__table__.columns[column].name] = int(value)
            elif self.__table__.columns[column].type == "NUMERIC":
                data[self.__table__.columns[column].name] = float(value)
            elif self.__table__.columns[column].type == "Decimal":
                data[self.__table__.columns[column].name] = float(value)
            elif self.__table__.columns[column].type == "time":
                data[self.__table__.columns[column].name] = str(value.strftime('%H:%M:%S'))
            elif self.__table__.columns[column].type == "datetime":
                data[self.__table__.columns[column].name] = str(value.strftime('%H:%M:%S'))
            else:
                data[self.__table__.columns[column].name] = str(value)
        return data
if __name__ == '__main__':
    GetProducts()


