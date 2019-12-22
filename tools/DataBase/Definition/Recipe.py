from sqlalchemy import Column, BIGINT, Text, MetaData, Table
from sqlalchemy.dialects.oracle.base import DOUBLE_PRECISION

from tools.DataBase.Connect import conection
from tools.DataBase.Definition.Base import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import ForeignKey

from tools.DataBase.Definition.Item import Item
from tools.DataBase.Definition.Status import Status
from tools.DataBase.Definition.company import company
from tools.main.general import general


class Recipe(Base):
    metadata = MetaData()

    __tablename__ = "recepie_reg"

    __table_args__ = {"useexisting": True}

    id = Column('id', BIGINT, primary_key=True)
    code = Column("code", BIGINT, nullable=False)
    item = Column("item", BIGINT, ForeignKey(Item.code), nullable=True)
    directions = Column("directions", Text, nullable=True)
    notes = Column("notes", Text, nullable=True)
    commerce = Column("company", ForeignKey(company.code), nullable=True)
    status = Column('status', BIGINT, ForeignKey(Status.code), nullable=True, default=12)

    # Relationship
    status_rel_cmp = relationship(Status, backref=backref("Recipe"))
    contact_rel_cmp = relationship(Item, backref=backref("Recipe"))
    company_rel_cmp = relationship(company, backref=backref("Recipe"))

    Recepie_tbl = Table(__tablename__, metadata, id, code, item,
                        directions, notes, status, commerce)

    def __repr__(self):
        return "<Recepie (id='%s', code='%s', item='%s', directions='%s'," \
               "notes='%s', status='%s', commerce='%s')>" % \
               (self.id, self.code, self.item,
                self.directions,self.notes, self.status, self.commerce)


if __name__ == '__main__':
    Recipe()

__author__ = 'hidura'
