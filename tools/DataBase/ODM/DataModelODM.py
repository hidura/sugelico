#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
'''
Created on Jan 2, 2015

@author: hidura
'''
from mongoengine import Document, LongField, StringField, DateTimeField, BooleanField, SortedListField, DictField
from mongoengine.base.fields import ObjectIdField
from mongoengine.fields import FloatField

from tools.DataBase.CodeGenerator import CodeGen
from tools.DataBase.Connect import conection


# Example Class##############################
# class Cart(Document):
#     #Document that store the carts of every client
#     client = LongField(required=True)
#     product = LongField(required=True)
#     price = FloatField(required=True)
#     amount = FloatField(required=True)
#     notes = StringField(required=True, default="")
#     costs=FloatField(required=True, default=0.00)
#     taxes=FloatField(required=True, default=0.00)
# Example Class ##############################


class ProductInfo(Document):
    # All the products to be sell are listed in here.
    id = ObjectIdField()
    code = LongField(required=True)
    price = FloatField(required=True)
    tax = FloatField(required=True)
    category = LongField(required=True)
    status = LongField(required=True)
    created_by = LongField(required=True)
    created_date = LongField(required=True)


class ProductCompanion(Document):
    # Register all the companions for the product
    id = ObjectIdField()
    product = LongField(required=True)
    companion = LongField(required=True)
    status = LongField(required=True)
    created_by = LongField(required=True)
    created_date = LongField(required=True)

class recipe_items(Document):
    code = LongField(required=True)
    recipe = LongField(required=True)# Product to be created
    item = LongField(required=True)# Item that compouse the product.
    item_name = StringField(required=True)  # Item that compouse the product.
    unit = LongField(required=True)
    unit_name = StringField(required=True)
    amount = FloatField(required=True)
    status = LongField(required=True, default=11)

class recipe_description(Document):
    # The description, of the content on every recipe
    id = ObjectIdField()
    recipe = LongField(required=True)
    item = LongField(required=True)
    amount = FloatField(required=True)
    unit = LongField(required=True)
    status = LongField(required=True)
    created_by = LongField(required=True)
    created_date = LongField(required=True)


class recipe_deduction(Document):
    # The description of every reduction on the recipe for every sale.
    id = ObjectIdField()
    recipe = LongField(required=True)
    item = LongField(required=True)
    amount = FloatField(required=True)
    unit = LongField(required=True)
    status = LongField(required=True)
    created_by = LongField(required=True)
    created_date = LongField(required=True)


class item_buy(Document):
    price = FloatField(required=True, default=0.00)
    item = LongField(required=True)
    bill = LongField(required=True, default=0)
    amount = FloatField(required=True)

class ncf_codes(Document):
    # The codes of the NCF used and not used
    code =LongField(required=True)
    secuence = StringField(required=True)
    ncf_type = LongField(required=True)
    status = LongField(required=True)
    exp = StringField(default="")

class ncfType(Document):
    # The types of NCF that have the database.
    code = LongField(required=True)
    name = StringField(required=True)
    header = StringField(required=True)
    serie = StringField(required=True)# Tipo de negocio.
    bdivision = StringField(required=True)# Division del negocio.
    pemission = StringField(required=True)# Punto de emision
    parea = StringField(required=True)# Area de impresion.
    _type = StringField(required=True)# NCF Type.


class PreOrder(Document):
    # The preOrder, of some product
    code = LongField(required=True)
    order = LongField(required=True)#This field is just for satisfy the necesity of the order field on the tablet.
    order_type = LongField(required=True)
    created_by = LongField(required=True)
    cashbox=LongField(required=True, default=1)
    created_date = LongField(required=True)
    client = LongField(required=False)
    cl_name =StringField(required=False, default="GENERICO")
    rnc = StringField(required=False, default="0000000")
    reference = StringField(required=False, default="0000000")
    _address=StringField(required=False, default="")
    telephone=StringField(required=False, default="--")
    ncf_type=StringField(required=False, default="02")
    total = FloatField(required=True, default=0.00)
    current_credit = FloatField(required=False, default=0.00)
    credit=BooleanField(required=False, default=False)
    max_credit = FloatField(required=False, default=0.00)
    status = LongField(required=True, default=11)


class ProductPre(Document):
    # Products on the PreOrder.
    code = LongField(required=True)
    preorder = LongField(required=True)
    product = LongField(required=True)
    product_name=StringField(required=False)
    amount = FloatField(required=True)
    notes = StringField(required=True)
    companion = StringField(required=True, default="")
    term = StringField(required=True)
    portion = StringField(required=True)
    saveit=LongField(required=True, default=1)
    subtotal = FloatField(required=True, default=0.00)
    tax = FloatField(required=True, default=0.00)
    total = FloatField(required=True, default=0.00)
    discount = FloatField(required=True, default=0.00)
    status = LongField(required=True, default=31)
    created_by = LongField(required=True)
    created_hour = LongField(required=False)
    created_date = LongField(required=True)
    client = StringField(required=True, default="Generico")


class ProductPreCompanion(Document):
    # Companion of the Products on the preorder
    id = ObjectIdField()
    preorder = LongField(required=True)
    product = LongField(required=True)
    companion = LongField(required=True)


class ProductPreCompound(Document):
    # Compounds of the preorder
    id = ObjectIdField()
    preorder = LongField(required=True)
    product = LongField(required=True)
    compound = LongField(required=True)


class PreOrderTable(Document):
    # Table assigned to the PreOrder
    preorder = LongField(required=True)
    table_code = LongField(required=True)
    people_on = LongField(required=True)# Number of people on the table.
    status = LongField(required=True, default=24)
    tbl_name=StringField(required=False)


class SaleTable(Document):
    # This class store the code of the sale,
    # and the tablet that is on that sale
    # After the sale is done.
    code = LongField(required=True)
    sale = LongField(required=True)
    table = LongField(required=True)
    status = LongField(required=True, default=24)
    amount_people = LongField(required=True)


class ProductSale(Document):
    # The items bought on by the company
    code = LongField(required=True)
    product_precode=LongField()# The code on the product_pre table.
    preorder=LongField(required=True)
    bill = LongField(required=True)
    product_name=StringField(required=True, default="")
    product = LongField(required=True)
    amount = FloatField(required=True)
    notes = StringField(required=True)
    term = StringField(required=True)
    cashbox = LongField(required=True, default=0)
    portion = StringField(required=True)
    subtotal = FloatField(required=True, default=0.00)
    tax = FloatField(required=True, default=0.00)
    total = FloatField(required=True, default=0.00)
    status = LongField(required=True, default=11)
    created_by = LongField(required=True)
    created_date = LongField(required=True)


class ConsumeDeferred(Document):
    # Class that store the Consumed deferred of the user
    code=LongField(required=True)
    client = LongField(required=True)
    amount_consumed = FloatField(required=True)
    product_consumed = LongField(required=True)
    consume_date = LongField(required=True)
    registred_by = LongField(required=True)
    credit_note = LongField(required=False)# This is just necessary if the user comes with a credit note.

class ProductSaleCompanion(Document):
    # Companion of the Product on the sale
    id = ObjectIdField()
    preorder = LongField(required=True)
    product = LongField(required=True)
    companion = LongField(required=True)


class ProductSaleCompound(Document):
    # Compound of products to sale
    id = ObjectIdField()
    preorder = LongField(required=True)
    product = LongField(required=True)
    compound = LongField(required=True)

class InputSale(Document):
    input_=LongField(required=True)
    amount_input=FloatField(required=True)
    product=LongField(required=True)
    amount_product=FloatField(required=True)
    created_by=LongField(required=True)
    created_date = LongField(required=True)


class Buyitems(Document):
    # The items bought on by the company
    code = LongField(required=True)
    bill = LongField(required=True)
    product = LongField(required=True)
    unit = LongField(required=True)
    amount = FloatField(required=True)
    notes = StringField(required=False)
    term = StringField(required=False)
    portion = StringField(required=False)
    subtotal = FloatField(required=True, default=0.00)
    tax = FloatField(required=True, default=0.00)
    total = FloatField(required=True, default=0.00)
    status = LongField(required=True, default=11)
    created_by = LongField(required=True)
    created_date = LongField(required=True)

class Equivalence(Document):
    # Is the definition in numbers from what the system is going to multiply every item
    # When the bill is deducted or the bill is added
    code = LongField(required=True)
    eq_name=StringField(default="")
    optype=StringField(required=True)
    from_eq = LongField(required=True)
    to_eq = LongField(required=True)
    equivalence = FloatField(required=True)
    created_by = LongField(required=True)
    created_date = LongField(required=True)
    status = LongField(required=True, default=11)

class Buybills_payment(Document):
    # The Payments of the bills of sale
    id = ObjectIdField()
    code = LongField(required=True)
    total_paid = FloatField(required=True)
    total_left = FloatField(required=True)
    pay_date = LongField(required=True)
    created_by = LongField(required=True)
    created_date = LongField(required=True)


class Salebills_payment(Document):
    # The payments of the bill that are
    code = LongField(required=True)
    total = FloatField(required=True)
    bill =LongField(required=True)
    pay_type = LongField(required=True)
    created_by = LongField(required=True)
    created_date = LongField(required=True)



class ContactHist(Document):
    # The copy of the contact information
    # to be easy access on an elastic search
    id = ObjectIdField()
    name = StringField(required=True)
    code = LongField(required=True)
    created_by = LongField(required=True)
    telephone = StringField(required=True)
    contact = LongField(required=True)
    last_name = StringField()
    cellphone = StringField()
    address = StringField()
    email = StringField()
    country = LongField()
    birthdate = LongField()
    idDocument = StringField()
    doc_type = StringField()
    created_date = LongField(required=True)
    meta = {"db_alias": "default"}


class UserInfo(Document):
    # Another information, that can be store of every User
    # that handle platea.
    id = ObjectIdField()
    client = LongField(required=True)
    value = StringField(required=True)
    code = LongField(required=True)
    created_by = LongField(required=True)
    created_date = LongField(required=True)
    meta = {"db_alias": "default"}


class UsertypeMenu(Document):
    # The class that store the relation between the type of user and the menu
    user_type = LongField(required=True)
    module = LongField(required=True)
    created_by = LongField(required=True)
    created_date = LongField(required=True)


class UserModule(Document):
    # The class that store the relation between the type of user and the menu
    user= LongField(required=True)
    module = LongField(required=True)
    created_by = LongField(required=True)
    created_date = LongField(required=True)
    status=LongField(required=True, default=11)
    module_name = StringField(required=True)
    group = LongField(required=True)
    group_name = StringField(required=True)


class UserArea(Document):
    #The association between the user and the area.
    user_code = LongField(required=True)
    area = LongField(required=True)
    status = LongField(required=True, default=11)


class UserMenu(Document):
    # The class that store the relation between the user and the menu, just on special situations
    id = ObjectIdField()
    user = LongField(required=True)
    module = LongField(required=True)
    created_by = LongField(required=True)
    created_date = LongField(required=True)


class Module(Document):
    # Modules registred on the system.
    code = LongField(required=True)
    name = StringField(required=True)
    path = StringField(required=True)
    icon = StringField(required=True, default="fa fa-circle-o")
    created_by = LongField(required=True)
    group=LongField()
    created_date = LongField(required=True)
    status=LongField(required=True, default=11)


class discount(Document):
    product = LongField(required=True)
    amount_disc = LongField(required=True)
    start_hour = LongField(required=True)
    end_hour = LongField(required=True)
    days = StringField(required=True)
    status = LongField(required=True, default=11)

class Group_module(Document):
    # Group of modules, that can be associated
    code = LongField(required=True)
    name = StringField(required=True)
    icon = StringField(required=True, default="fa fa-circle-o")
    created_by = LongField(required=True)
    status=LongField(required=True, default=11)
    group=LongField(required=False, default=0)
    created_date = LongField(required=True)

class group_module_asc(Document):
    module = LongField(required=True)
    group = LongField(required=True)

class SessionUser(Document):
    # This document, save the information of the session
    # of any user.
    login = LongField(required=True)
    logout = LongField()
    status = LongField(required=True, default=31)
    userCode = LongField(required=True)
    usertype = LongField(required=True, default=0)
    logType = LongField(required=True, default=0)
    code = LongField(required=True)
    created_by = LongField(required=True)
    created_date = LongField(required=True)
    meta = {"db_alias": "default"}


class printer_reg(Document):
    code = LongField(required=True)
    status = LongField(required=True, default=11)
    company = LongField(required=True)
    brand = StringField(required=False)
    model = StringField(required=False)
    server = StringField(required=False)
    path = StringField(required=False)
    name = StringField(required=False)
    username = StringField(required=False)
    password = StringField(required=False)
    _type = LongField(required=False)
    category = StringField(required=False)#Just for the printers of cousine or bar.



class SessionUserSys(Document):
    # The sessions of the user that work with the system.
    id = ObjectIdField()
    login = DateTimeField(required=True)
    logout = DateTimeField(required=True)
    status = LongField(required=True)
    created_by = LongField(required=True)
    created_date = LongField(required=True)
    code = StringField(required=True, default=CodeGen().GenCode({"table": "SessionUserSys"}))
    meta = {"db_alias": "default"}


class waiterKey(Document):
    code = LongField(required=True)
    user_code = LongField(required=True)
    key = StringField(required=True)
    status = LongField(required=True, default=11)
    created_by = LongField(required=True)
    created_date = LongField(required=True)


class Country(Document):
    code = LongField(required=True)
    name = StringField(required=True)
    countryCode = StringField(required=True)


class PreOrderProdDel(Document):
    code = LongField(required=True)
    preorder = LongField(required=True)
    product = LongField(required=True)
    amount = FloatField(required=True)
    status = LongField(required=True, default=16)
    reason = StringField(required=True)
    created_by = LongField(required=True)
    created_date = LongField(required=True)
    approved_by=LongField(required=False)

class MermaProd(Document):
    code = LongField(required=True)
    product = LongField(required=True)
    amount = FloatField(required=True)
    merma=LongField(required=True)


class Moveproducts(Document):
    code = LongField(required=True, default=0)
    give_by = LongField(required=True, default=0)
    receive_by = LongField(required=True, default=0)
    product=LongField(required=True)
    created_date = LongField(required=True)
    description=StringField()

class account_movement(Document):
    code=LongField(required=True)
    amount = FloatField(required=True, default=0.00)
    credit = LongField(required=False)
    credit_name=StringField()
    credit_code=LongField()
    debit = LongField(required=True)
    debit_name=StringField()
    debit_code=LongField()
    register_date = LongField(required=True)
    notes = StringField(required=True)



class PrepProducts(Document):
    # Products preparared on the restaurant,
    # that will be add to another product.
    preparation = LongField(required=True)
    code = LongField(required=True)
    product = LongField(required=True)
    amount = FloatField(required=True)
    services = FloatField(required=True)
    created_date = LongField(required=True)
    description=StringField()



class products_move(Document):
    code = LongField(required=True)
    product = LongField(required=True)
    amount = FloatField(required=True)


# The additional products
class product_additional(Document):
    product = LongField(required=True)
    additional = LongField(required=True)
    status = LongField(required=True, default=11)
    cycle = LongField(required=False)
    name=StringField()
    price=FloatField()


# The open cashBox
class cashbox_open(Document):
    status = LongField(required=True)
    code =LongField(required=True)
    amount_open = FloatField(required=True)
    user_opened= LongField(required=True, default=1)#Este campo es necesario, porque sin el por algun extra�o motivo no funciona nada en el viejo sistema.
    amount_close=FloatField(required=False, default=0.00)
    open_date = LongField(required=True)
    close_date=LongField(required=False)
    cashbox = LongField(required=True)


class cashbox_bills(Document):
    cashbox = LongField(required=True)
    bill = LongField(required=True, default=1)
    total = FloatField(required=True)
    preorder = LongField(required=True)
    ncf = StringField(required=False)
    paytype = LongField(required=True)
    registred = LongField(required=True)
    printed = LongField(required=True, default=0)



# The Optionals products
class product_optionals(Document):
    product = LongField(required=True)
    optional = LongField(required=True)
    status = LongField(required=True, default=11)
    cycle = LongField(required=False)
    name = StringField()
    price = FloatField()

# The Compounds products
class product_compounds(Document):
    product = LongField(required=True)
    compound = LongField(required=True)
    status = LongField(required=True, default=11)
    cycle = LongField(required=False)
    name = StringField()
    price = FloatField()


class product_term(Document):
    # Association between the product and the term.
    product = LongField(required=True)
    term = LongField(required=True)
    status = LongField(required=True, default=11)
    name = StringField(required=True)


class terms(Document):
    # Store the terms of the meals
    code = LongField(required=True)
    _name = StringField(required=True)
    notes = StringField()

class cashbox(Document):
    code = LongField(required=True)
    _name = StringField(required=True)
    warehouse = LongField(required=False, default=1)
    company = LongField(required=True, default=1)
    branch = LongField(required=True, default=1)
    status = LongField(required=True, default=11)
    description = StringField(required=True, default="")
    user_owner = LongField(required=True)
    printer = LongField(required=True, default=1)# The printer information of the printer installed on the cashbox.

class UserCompany(Document):
    user_code = LongField(required=True)
    company = LongField(required=True)
    name_cmp = StringField()
    telephone_cmp = StringField()
    address_cmp = StringField()
    rnc_cmp = StringField()
    otherfields_cmp = StringField()


class archieve_preorder(Document):
    preorder = LongField(required=True)
    reason = StringField(required=True)
    created_by = LongField(required=True)
    created_date = LongField(required=True)
    created_hour = LongField(required=True)

class tabReguster(Document):
    token_id = StringField()
    brand = StringField(required=True)
    model = StringField(required=True)
    android_ver = StringField()
    company = LongField(required=True)
    manufacturer = StringField()
    serial = StringField()


class Bill2Print(Document):
    # Bills that are ready to be printed.
    bill = LongField(required=True, unique=True)
    preorder = LongField(required=True)
    cashbox = LongField(required=True)

class warehouse_prods(Document):
    code=LongField(required=True)
    warehouse = LongField(required=True)
    product=LongField(required=True)
    amount=FloatField(required=True)
    status=FloatField(required=True, default=11)


class ProductTax(Document):
    product=LongField(required=True)
    tax=LongField(required=True)

class tax(Document):
    code = LongField(required=True)
    percent=FloatField(required=True)
    name=StringField(required=True)

class paytype_det(Document):
    code=LongField(reference=False)
    typid = LongField(required=True)
    denomination = DictField(required=False)
    reference = BooleanField(required=True, default=False)
    percent_extra=FloatField(required=True, default=0.00)

class billtype_det(Document):
    typid = LongField(required=True)
    reference = BooleanField(required=False, default=False)
    percent_extra=FloatField(required=False, default=0.00)


class product_req(Document):
    # These are the products that are in a Requisition.
    code = LongField(required=True)
    bill = LongField(required=True)
    product = LongField(required=True)
    unit = LongField(required=False)
    amount = FloatField(required=False)
    status = LongField(required=False, default=18)
    created_by = LongField(required=False)
    created_date = LongField(required=False)


class sysrules(Document):
    # These are the rule of the system.
    code = LongField(required=True)
    name = StringField(required=True)
    description = StringField(required=True)

class rule_user(Document):
    # The users that have granted the permission of the rule.
    rule_code = LongField(required=True)
    user_code = LongField(required=True)
    rule_name=StringField(required=True)

class rules_company(Document):
    # The users that have granted the permission of the rule.
    rule_code = LongField(required=True)
    company_code = LongField(required=True)
    rule_name=StringField(required=True)

# HELPER AREA##########################################
# Here I complete some table that were designed in
# a way and now change it will brake the system apart
class product_type(Document):

    prod_type = LongField(required=True)
    avatar = StringField(required=False, default="dinner.png")


if __name__ == '__main__':
    ###Testing area
    myConn = conection().conODM()
    print(Module.objects())
    #UsertypeMenu.objects(id='579cc3748f01b939d41efe0a').delete()
    # code = CodeGen().GenCode({"table": "printer", "column": "code"})
    # printer_reg(code=code, brand="Smart & Cool", model="POS-5890C", papersize=58).save()
    # code = CodeGen().GenCode({"table": "printer", "column": "code"})
    # printer_reg(code=code, brand="Star", model="SP200", papersize=90).save()

    # code = CodeGen().GenCode({"table": "cashbox", "column": "code"})
    #
    # cashbox(_name="001", code=code, company=3, branch=1, description="Caja del piso principal.", printer=1).save()
    # #UsertypeMenu.objects(id="579cc3748f01b937b857915c").update(set__module=21)
    # UsertypeMenu(user_type=74, module=21, created_by=11, created_date=2457634).save()
    # for piece in UsertypeMenu.objects(user_type=74):
    #     print(piece.user_type, piece.module, piece.id, piece.created_by, piece.created_date)
    # for piece in Module.objects():
    #     print(piece.code, piece.name, piece.path, piece.id)


    # for piece in ProductPre.objects(preorder=78):
    #     print(piece.preorder)
    # for waiter in waiterKey.objects():
    #     print(waiter.key, waiter.user_code)
    # ncftypelst=[{"name":"Facturas que generan Cr�dito y Sustentan Costos y/o Gastos",
    #             "serie":"A","bdivision":"01","pemission":"001","parea":"001","_type":"01",
    #             "header":"A0100100101"}, {"name":"Facturas para Consumidores Finales",
    #             "serie":"A","bdivision":"01","pemission":"001","parea":"001","_type":"02",
    #             "header":"A0100100102"},{"name":"Nota de D�bito",
    #             "serie":"A","bdivision":"01","pemission":"001","parea":"001","_type":"03",
    #             "header":"A0100100103"},{"name":"Nota de Cr�dito",
    #             "serie":"A","bdivision":"01","pemission":"001","parea":"001","_type":"04",
    #             "header":"A0100100104"},{"name":"Proveedores Informales",
    #             "serie":"A","bdivision":"01","pemission":"001","parea":"001","_type":"11",
    #             "header":"A0100100111"},{"name":"Registro �nico de Ingresos",
    #             "serie":"A","bdivision":"01","pemission":"001","parea":"001","_type":"12",
    #             "header":"A0100100112"},{"name":"Gastos Menores",
    #             "serie":"A","bdivision":"01","pemission":"001","parea":"001","_type":"13",
    #             "header":"A0100100113"},
    #             {"name":"Reg�menes Especiales de Tributaci�n",
    #             "serie":"A","bdivision":"01","pemission":"001","parea":"001","_type":"14",
    #             "header":"A0100100114"}]
    #
    # ncfLst = {"01":[1,5001],
    #           "02":[1,5001],
    #           "03":[1,5001],
    #           "04":[1,5001],
    #           "11":[1,5001],
    #           "12":[1,5001],
    #           "13":[1,5001],
    #           "14":[1,5001]}
    # for piece in ncftypelst:
    #     # code = LongField(required=True)
    #     # name = StringField(required=True)
    #     # header = StringField(required=True)
    #     # serie = StringField(required=True)  # Tipo de negocio.
    #     # bdivision = StringField(required=True)  # Division del negocio.
    #     # pemission = StringField(required=True)  # Punto de emision
    #     # parea = StringField(required=True)  # Area de impresion.
    #     # _type = StringField(required=True)  # NCF Type.
    #     #print(piece._type, piece.name, piece.header)
    #     code=CodeGen().GenCode({"table":"ncfType", "column":"code"})
    #     ncfType(code=code, name=piece["name"], header=piece["header"],
    #             serie=piece["serie"], bdivision=piece["bdivision"],
    #             pemission=piece["pemission"], parea=piece["parea"],
    #             _type=piece["_type"]).save()
    #     if piece["_type"] in ncfLst:
    #         for cont in range(ncfLst[piece["_type"]][0], ncfLst[piece["_type"]][0]):
    #             # code = LongField(required=True)
    #             # secuence = StringField(required=True)
    #             # ncf_type = LongField(required=True)
    #             # status = LongField(required=True)
    #             _code = CodeGen().GenCode({"table": "ncf_codes", "column": "code"})
    #             ncf_codes(code=_code, secuence=str(cont).zfill(8), ncf_type=code, status=14).save()
    # code = LongField(required=True)
    # optype = StringField(required=True)
    # from_eq = LongField(required=True)
    # to_eq = LongField(required=True)
    # equivalence = FloatField(required=True)
    # created_by = LongField(required=True)
    # created_date = LongField(required=True)
    # status = LongField(required=True, default=11)
    # for ncf_type in ncfType.objects():
    #     print(ncf_type.code, ncf_type.name, ncf_type.header)
    #     for piece in ncf_codes.objects(ncf_type=ncf_type.code, status=15):
    #         print(piece.code, piece.ncf_type, piece.status, piece.secuence)
    # for piece in Module.objects():
    #     print(piece.name, piece.path)
    # myConn.disconnect()
    # ncfType.objects(code=12).update(set__header="A0100100102")
    # ncfType.objects(code=11).update(set__header="A0100100101")
    #ncf_codes.objects(ncf_type=12, code=14161).update(set__status=11)

    # ProductPre.objects(code=4243).update(set__discount=125.00)
    # ProductPre.objects(code=4244).update(set__discount=135.00)
    # ProductPre.objects(code=4245).update(set__discount=130.00)
    # ProductPre.objects(code=3933).update(set__preorder=716)
    # ProductPre.objects(code=3934).update(set__preorder=716)
    # ProductPre.objects(code=3935).update(set__preorder=716)

    #ProductPre.objects(code=3838).update(set__discount=85.00)

    #print(PreOrderTable.objects(table_code=38).order_by('-preorder').first().preorder)
    # ProductPre.objects(code=2409).update(set__discount=90.00)
    # ncf_codes.objects(id="587d17a722176615f06fe8e0").update(set__status=15)
    # ncfLst = {12:[32365,40000], 11:[9776,15010],15:[12,600]}
    # ncfLst = {12: [34255, 40000], 11:[8418,15010], 15: [12, 600]}
    # for tpncf in ncfLst:
    #     for new_code in range(ncfLst[tpncf][0],ncfLst[tpncf][1]):
    #         code = CodeGen().GenCode({"table":"ncf_codes", "column":"code"})
    #
    #         data = ncf_codes(code=code, secuence=str(new_code).zfill(8), ncf_type=tpncf, status=11).save()
    #         print(data.secuence)
    # None
__author__ = 'hidura'
